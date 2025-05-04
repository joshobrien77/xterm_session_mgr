#!/usr/bin/env python3
"""iTerm2 Session Manager (menu-only)"""

import asyncio, json, subprocess
from pathlib import Path
import iterm2

SESSION_FILE = Path.home() / ".iterm2_sessions.json"

def load_sessions():
    return json.loads(SESSION_FILE.read_text())

def build_applescript(s):
    cmd = f'ssh -i "{s.get("identityFile","")}" {s["user"]}@{s["host"]}'
    if s.get("launchMode","newWindow") == "newWindow":
        return f"""
tell application "iTerm2"
  create window with default profile
  tell current session of current window to write text "{cmd}"
end tell
""".strip()
    else:
        return f"""
tell application "iTerm2"
  tell current window
    create tab with default profile
    tell current session to write text "{cmd}"
  end tell
end tell
""".strip()

async def run(connection):
    sessions = load_sessions()

    for sess in sessions:
        item = iterm2.MenuItem(sess["name"])
        @iterm2.LaunchAsyncMenuItem(connection, item)
        async def _launch(_item, _ctx, sess=sess):
            applescript = build_applescript(sess)
            subprocess.run(["osascript", "-e", applescript])

    reload_item = iterm2.MenuItem("Reload Sessions")
    @iterm2.LaunchAsyncMenuItem(connection, reload_item)
    async def _reload(_item, _ctx):
        await run(connection)

    await asyncio.Future()

if __name__ == "__main__":
    iterm2.run_forever(run)
