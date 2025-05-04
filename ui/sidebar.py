# ui/sidebar.py

import asyncio
import iterm2
from executor import launch_session_via_applescript
from config import Session
from typing import List

async def setup_sidebar(connection, sessions: List[Session]) -> iterm2.SidebarAsync:
    """
    Create (or reuse) the Session Manager sidebar, populate it with
    the given sessions, and return the sidebar object.
    """
    # Create the sidebar (tool) if needed
    sidebar = await iterm2.SidebarAsync(connection,
                                        name="Session Manager",
                                        tool="session_manager")

    # Clear out old items (in case of reload)
    await sidebar.async_clear_items()

    # Add one entry per session
    for sess in sessions:
        # Define a handler that captures this sess
        async def handler(menu_item, ctx, sess=sess):
            # Launch via our executor
            result = launch_session_via_applescript(sess)
            if result.returncode != 0:
                # Show an alert on failure
                await iterm2.Alert("Session Manager",
                                   f"Failed to launch {sess.name}:\n{result.stderr}",
                                   connection=connection)
        # Add it to the sidebar
        await sidebar.async_add_item(title=sess.name,
                                     handler=handler)
    return sidebar
