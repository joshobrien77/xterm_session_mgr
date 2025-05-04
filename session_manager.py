#!/usr/bin/env python3
# session_manager.py

import asyncio
import iterm2
import json
from config import load_sessions, Session
from executor import launch_session_via_applescript

# Path to your JSON session file
SESSION_FILE = os.path.expanduser("~/.iterm2_sessions.json")

async def run(connection):
    # 1. Load sessions
    sessions = load_sessions(SESSION_FILE)

    # 2. Create a sidebar tool window
    app = await iterm2.async_get_app(connection)
    sidebar = await iterm2.SidebarAsync(connection,
        name="Session Manager",
        tool="session_manager"
    )

    # Populate the sidebar with session entries
    for sess in sessions:
        item = await sidebar.async_add_item(
            title=sess.name,
            handler=lambda: asyncio.ensure_future(on_select(sess))
        )
        # Optionally set icons, badges, etc.

    # 3. Hook up a menu item to show/hide the sidebar
    menu = iterm2.MenuItem("Session Manager → Toggle Sidebar")
    @iterm2.LaunchAsyncMenuItem(connection, menu)
    async def toggle_sidebar(menu_item, ctx):
        if sidebar.is_shown:
            await sidebar.async_hide()
        else:
            await sidebar.async_show()

    await iterm2.Future()  # Keep the script running

async def on_select(session: Session):
    # Called when a user selects a session from the sidebar
    # Launch it via our executor
    result = launch_session_via_applescript(session)
    if result.returncode != 0:
        # Optionally pop up an alert
        print("Error launching session:", result.stderr)

if __name__ == "__main__":
    iterm2.run_forever(run)
