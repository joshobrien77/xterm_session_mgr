# tests/test_launcher.py
import pytest
from config import Session
from launcher import generate_applescript, LaunchMode

@pytest.mark.parametrize("mode, marker", [
    ("newWindow",   "create window with default profile"),
    ("newTab",      "create tab with default profile"),
    ("splitPane",   "split horizontally with default profile"),
])
def test_generate_applescript(mode, marker):
    sess = Session(
        id="1",
        name="Test",
        host="host.example.com",
        port=22,
        user="alice",
        identity_file="~/.ssh/id_rsa",
        launch_mode=mode,
        password_key=None
    )
    script = generate_applescript(sess)
    # should contain the mode-specific marker...
    assert marker in script
    # ...and the SSH command
    assert 'ssh -i "~/.ssh/id_rsa" alice@host.example.com' in script

def test_generate_applescript_invalid_mode():
    sess = Session(
        id="1",
        name="Bad",
        host="host",
        port=22,
        user="bob",
        identity_file=None,
        launch_mode="no-such-mode",
        password_key=None
    )
    with pytest.raises(ValueError):
        generate_applescript(sess)
