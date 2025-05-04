# tests/test_executor.py

import subprocess
import pytest
from config import Session
from executor import launch_session_via_applescript

@pytest.fixture(autouse=True)
def capture_run(monkeypatch):
    calls = []
    def fake_run(args, capture_output, text):
        # Record the invocation
        calls.append({
            "args": args,
            "capture_output": capture_output,
            "text": text
        })
        # Simulate a successful osascript call
        return subprocess.CompletedProcess(args=args, returncode=0, stdout="ok", stderr="")
    monkeypatch.setattr(subprocess, "run", fake_run)
    return calls

def test_launch_session_invokes_osascript(capture_run):
    sess = Session(
        id="1",
        name="Test",
        host="host.example.com",
        port=22,
        user="alice",
        identity_file="~/.ssh/id_rsa",
        launch_mode="newTab",
        password_key=None
    )
    result = launch_session_via_applescript(sess)

    # Verify subprocess.run returned our fake CompletedProcess
    assert result.returncode == 0
    assert result.stdout == "ok"

    # Verify we invoked osascript exactly once
    assert len(capture_run) == 1
    run_call = capture_run[0]

    # Command should start with osascript
    assert run_call["args"][0] == "osascript"
    # The "-e" flag and a script string should be present
    assert "-e" in run_call["args"]
    script_arg = run_call["args"][run_call["args"].index("-e") + 1]
    # It should contain our SSH command
    assert 'ssh -i "~/.ssh/id_rsa" alice@host.example.com' in script_arg

def test_launch_session_invalid_mode_raises():
    # If we pass a Session with an invalid launch_mode into generate_applescript,
    # it should bubble up as a ValueError.
    bad = Session(
        id="1",
        name="Bad",
        host="host",
        port=22,
        user="bob",
        identity_file="~/.ssh/id_rsa",
        launch_mode="no-such-mode",
        password_key=None
    )
    with pytest.raises(ValueError):
        launch_session_via_applescript(bad)
