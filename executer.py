# executor.py

import subprocess
from config import Session
from launcher import generate_applescript

def launch_session_via_applescript(session: Session) -> subprocess.CompletedProcess:
    """
    Generate and run the AppleScript for `session` via the `osascript` CLI.
    Returns the CompletedProcess from subprocess.run.
    """
    script = generate_applescript(session)
    # Call osascript with the script
    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )
    return result
