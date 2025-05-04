# launcher.py
from enum import Enum
from config import Session

class LaunchMode(Enum):
    NEW_WINDOW = "newWindow"
    NEW_TAB    = "newTab"
    SPLIT_PANE = "splitPane"

def generate_applescript(session: Session) -> str:
    """
    Given a Session, return the AppleScript that will SSH into it
    in the configured launch mode.
    """
    cmd = f'ssh -i "{session.identity_file}" {session.user}@{session.host}'
    mode = LaunchMode(session.launch_mode)

    if mode == LaunchMode.NEW_WINDOW:
        script = f'''
tell application "iTerm2"
    create window with default profile
    tell current session of current window
        write text "{cmd}"
    end tell
end tell
'''.strip()

    elif mode == LaunchMode.NEW_TAB:
        script = f'''
tell application "iTerm2"
    tell current window
        create tab with default profile
        tell current session
            write text "{cmd}"
        end tell
    end tell
end tell
'''.strip()

    elif mode == LaunchMode.SPLIT_PANE:
        script = f'''
tell application "iTerm2"
    tell current window
        tell current session
            split horizontally with default profile
        end tell
        tell last session
            write text "{cmd}"
        end tell
    end tell
end tell
'''.strip()

    else:
        raise ValueError(f"Unknown launch mode: {session.launch_mode}")

    return script
