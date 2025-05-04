# xterm_session_mgr

A self-contained, menu-only session manager for iTerm2 3.5.x (GA).  
Reads session definitions from `~/.iterm2_sessions.json` and registers one menu item per session under **Scripts → session_manager_menu**.

## Repository Structure

```
xterm_session_mgr/
├── LICENSE
├── README.md
├── .gitignore
├── sessions-template.csv
├── session_manager_menu.py
├── config.py
├── applescript.py
└── tests/
    ├── test_config.py
    └── test_applescript.py
```

## Installation

1. Clone or download this repo:  
   ```bash
   git clone https://github.com/yourorg/xterm_session_mgr.git
   cd xterm_session_mgr
   ```
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
