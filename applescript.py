def build_applescript(sess):
    """Generate the AppleScript to SSH into a session dict."""
    cmd = f'ssh -i "{sess.get("identityFile","")}" {sess["user"]}@{sess["host"]}'
    if sess.get("launchMode","newWindow") == "newWindow":
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
