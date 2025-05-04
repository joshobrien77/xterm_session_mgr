#!/usr/bin/env python3
"""
session_manager_deploy.py

A self-contained iTerm2 Session Manager:
- Reads ~/.iterm2_sessions.json
- Builds a sidebar with Launch and Toggle controls
- Uses AppleScript to SSH into each host
"""

import os, json, pathlib, asyncio, subprocess, iterm2

# 1) Load sessions from home
SESSION_FILE = pathlib.Path.home() / ".iterm2_sessions.json"
def load_sessions():
    with open(SESSION_FILE) as f:
        return json.load(f)

# 2) Build the AppleScript for a session dict
def build_applescript(s):
    cmd = f'ssh -i "{s.get("identityFile","")}" {s["user"]}@{s["host"]}'
    lm = s.get("launchMode","newWindow")
    if lm == "newWindow":
        return f'''
tell application "iTerm2"
  create window with default profile
  tell current session of current window
    write text "{cmd}"
  end tell
end tell
'''.strip()
    else:
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

# 3) Main entrypoint
async def run(connection):
    # Load & clear
    sessions = load_sessions()
    sidebar = await iterm2.SidebarAsync(connection,
                                        name="Session Manager",
                                        tool="session_manager")
    await sidebar.async_clear_items()

    # Add an item per session
    for sess in sessions:
        async def handler(menu_item, ctx, sess=sess):
            script = build_applescript(sess)
            subprocess.run(["osascript","-e",script])
        await sidebar.async_add_item(title=sess["name"],
                                     handler=handler)

    # Add the Toggle menu
    toggle = iterm2.MenuItem("Toggle Sidebar")
    @iterm2.LaunchAsyncMenuItem(connection, toggle)
    async def _toggle(menu_item, ctx):
        if sidebar.is_shown:
            await sidebar.async_hide()
        else:
            await sidebar.async_show()

    await asyncio.Future()

# 4) Kick it off
if __name__ == "__main__":
    iterm2.run_forever(run)
