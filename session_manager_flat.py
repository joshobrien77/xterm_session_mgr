#!/usr/bin/env python3
"""
A self-contained iTerm2 session manager MVP.

This single file defines:
  - A hard‐coded demo session (replace with JSON loading later)
  - A “Toggle Sidebar” menu item
  - A sidebar with one entry that SSHes into demo.example.com
"""

import asyncio, iterm2
import subprocess

DEMO = {
    "name": "Demo Server",
    "host": "demo.example.com",
    "user": "alice",
    "identity_file": "~/.ssh/id_rsa",
    "launch_mode": "newTab"
}

def build_applescript(s):
    cmd = f'ssh -i "{s["identity_file"]}" {s["user"]}@{s["host"]}'
    if s["launch_mode"] == "newWindow":
        return f'''
tell application "iTerm2"
  create window with default profile
  tell current session of current window
    write text "{cmd}"
  end tell
end tell
'''.strip()
    else:  # newTab
        return f'''
tell application "iTerm2"
  tell current window
    create tab with default profile
    tell current session
      write text "{cmd}"
    end tell
  end tell
end tell
'''.strip()

async def run(connection):
    # Sidebar
    sidebar = await iterm2.SidebarAsync(connection,
                                        name="Session Manager",
                                        tool="session_manager_flat")
    await sidebar.async_clear_items()
    async def handler(menu_item, ctx):
        script = build_applescript(DEMO)
        subprocess.run(["osascript","-e",script])
    await sidebar.async_add_item(title=DEMO["name"],
                                 handler=handler)

    # Toggle menu
    toggle = iterm2.MenuItem("Toggle Sidebar")
    @iterm2.LaunchAsyncMenuItem(connection, toggle)
    async def _toggle(menu_item, ctx):
        if sidebar.is_shown:
            await sidebar.async_hide()
        else:
            await sidebar.async_show()

    await asyncio.Future()

if __name__ == "__main__":
    iterm2.run_forever(run)
