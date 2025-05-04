# XTerm Session Manager

A native macOS SwiftUI application that provides a GUI for managing and launching SSH sessions in iTerm2.

## Features

- **Session List**: Displays sessions loaded from a JSON file (`~/.iterm2_sessions.json`).
- **Launch Modes**: Open sessions in a new iTerm2 window or a new tab.
- **Runtime Reload**: Reload the session list without restarting the app.
- **Self-contained**: Uses AppleScript under the hood; no external dependencies beyond macOS and iTerm2.

## Requirements

- macOS 11.0 (Big Sur) or later
- Xcode 12 or later
- iTerm2 3.5.x (GA)

## Project Layout

```
xterm_session_mgr_app/
├── XTermSessionManager.xcodeproj
├── XTermSessionManager/
│   ├── AppDelegate.swift
│   ├── ContentView.swift
│   ├── Session.swift
│   ├── SessionStore.swift
│   └── AppleScriptExecutor.swift
├── Resources/
│   └── sessions-template.json
└── README.md
```

- **XTermSessionManager.xcodeproj**: Xcode project file.
- **XTermSessionManager/**: Swift source files.
- **Resources/**: Example JSON template.
- **README.md**: Project overview and instructions.

## Getting Started

1. **Clone the repository** (or unzip the scaffold).
2. **Open** `XTermSessionManager.xcodeproj` in Xcode.
3. **Build & Run** the `XTermSessionManager` scheme on **My Mac**.
4. The app will load sessions from `~/.iterm2_sessions.json` and display them in a window.
5. **Click** a session to launch it in iTerm2.

## Configuration

Edit (or create) `~/.iterm2_sessions.json` in your home directory using the following structure:

```json
[
  {
    "name": "Prod Web",
    "host": "web01.example.com",
    "user": "deploy",
    "identityFile": "~/.ssh/id_rsa",
    "launchMode": "newTab"
  },
  {
    "name": "Staging DB",
    "host": "db.staging.example.com",
    "user": "dba",
    "identityFile": "",
    "launchMode": "newWindow"
  }
]
```

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
