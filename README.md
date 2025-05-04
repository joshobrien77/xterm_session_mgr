# iTerm2 Session Manager Plugin

A native session‐manager plugin for [iTerm2](https://iterm2.com/) inspired by SecureCRT/MobaXterm.  
Manage, launch and organize your SSH sessions—complete with Keychain‐backed credentials, CSV import/export, and flexible launch modes—all from a dockable sidebar in iTerm2.

---

## 🚀 Features

- **Session Tree & Folders**  
  Organize sessions into folders, tags or favorites.

- **Launch Modes**  
  - New Window  
  - New Tab  
  - Split Pane  

- **Secure Credentials**  
  - Store passwords/passphrases in macOS Keychain  
  - Optional prompt + “always allow” access  
  - Extensible to other stores (1Password CLI, etc.)

- **Config-Driven**  
  - JSON (or YAML) session definitions  
  - Optional parsing of `~/.ssh/config`  

- **CSV Import/Export**  
  - Bulk-import your session list from a CSV template  
  - Export selected sessions for sharing or backup  

- **Lightweight & Native**  
  - Written in Python using the iTerm2 Async API  
  - Minimal dependencies (Python 3.8+, `iterm2`, `keyring`, `PyYAML`/`json`)

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourorg/iterm2-session-manager.git
   cd iterm2-session-manager
   ```

2. **Install dependencies**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install iterm2 keyring PyYAML
   ```

3. **Install as iTerm2 script**  
   Copy the `session_manager.py` script into:
   ```
   ~/Library/Application Support/iTerm2/Scripts/
   ```
4. **Enable Python API**  
   In iTerm2 → Preferences → General → “Magic” → enable **“Load iTerm2 Python API”**.

5. **Reload scripts**  
   In iTerm2 → Scripts → “Refresh Scripts”.

---

## ⚙️ Configuration

1. **Session JSON**  
   Create (or edit) `~/.iterm2_sessions.json`:
   ```jsonc
   [
     {
       "id": "prod-web",
       "name": "Production Web",
       "host": "web01.example.com",
       "port": 22,
       "user": "deploy",
       "identityFile": "~/.ssh/id_rsa",
       "launchMode": "newTab",
       "passwordKey": "prod-web@example.com"
     }
   ]
   ```

2. **Keychain Setup**  
   Store a password or passphrase:
   ```python
   import keyring
   keyring.set_password("iterm2-session-manager", "prod-web@example.com", "MyS3cret!")
   ```

3. **CSV Template**  
   Download and edit `sessions-template.csv`:
   ```csv
   Name,Host,Port,Username,KeyPath,PasswordKey,LaunchMode
   Prod Web,web01.example.com,22,deploy,~/.ssh/id_rsa,prod-web@example.com,newTab
   ```
   Then import via the plugin’s “Import CSV” menu.

---

## 🖥️ Usage

1. Open iTerm2.  
2. In the Scripts menu, choose **Session Manager → Show Sidebar**.  
3. Browse your session tree; double-click or right-click → **Launch**.  
4. Toggle “New Tab” / “New Window” in the sidebar’s toolbar per session.

---

## 🛠️ Development

- **Code Layout**  
  ```
  ├── session_manager.py    # Main plugin entrypoint
  ├── config.py             # JSON/YAML loader & model
  ├── keychain.py           # Keychain get/set wrappers
  ├── csv_tools.py          # CSV import/export handlers
  └── ui/                   # Sidebar & dialogs (iTerm2 Python API)
  ```

- **Run Locally**  
  ```bash
  iterm2 --debug --scripts ~/path/to/iterm2-session-manager/
  ```

- **Testing**  
  ```bash
  pytest tests/
  ```

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feat/my-feature`)  
3. Commit your changes (`git commit -m "Add …"`)  
4. Push (`git push origin feat/my-feature`)  
5. Open a Pull Request


## 📜 License

This project is licensed under the **Apache License 2.0**.  
See the [LICENSE](LICENSE) file for details.
