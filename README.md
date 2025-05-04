# iTerm2 Session Manager (Menu-Only)

A self-contained, menu-only session manager for iTerm2 3.5.x (GA).  
Reads session definitions from `~/.iterm2_sessions.json` and registers one menu item per session under **Scripts → session_manager_menu**.

## Files

- **session_manager_menu.py**: Entry-point Python script to import into iTerm2.
- **config.py**: Helper module for loading the JSON sessions file.
- **applescript.py**: Helper module to generate AppleScript for SSH launch.
- **sessions-template.csv**: CSV template for bulk session import (optional).
- **tests/**: Pytest tests for `config.py` and `applescript.py`.

## Installation

1. Clone or download this repo.  
2. Ensure your JSON session file exists at `~/.iterm2_sessions.json`.  
3. In iTerm2: **Scripts → Manage → Import Python Script…** and select `session_manager_menu.py`.  
4. Restart iTerm2 (⌘Q → reopen).  

## Usage

Under the **Scripts** menu you’ll see:

```
session_manager_menu ▶  
    <Session Name 1>  
    <Session Name 2>  
    Reload Sessions  
```

- **Click a session name** to open a new tab/window via SSH.  
- **Click Reload Sessions** to re-read the JSON file without restarting iTerm2.

## Running Tests

```bash
pytest tests/
```

## License

Apache License 2.0
