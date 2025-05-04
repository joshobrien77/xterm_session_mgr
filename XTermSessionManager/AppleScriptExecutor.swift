import Foundation
import Cocoa

class AppleScriptExecutor {
    static func run(_ session: Session) {
        let identity = session.identityFile ?? "~/.ssh/id_rsa"
        let cmd = "ssh -i \"\(identity)\" \(session.user)@\(session.host)"
        let script: String
        if session.launchMode == "newWindow" {
            script = """
tell application "iTerm2"
  create window with default profile
  tell current session of current window to write text "\(cmd)"
end tell
"""
        } else {
            script = """
tell application "iTerm2"
  tell current window
    create tab with default profile
    tell current session to write text "\(cmd)"
  end tell
end tell
"""
        }
        var error: NSDictionary?
        if let apple = NSAppleScript(source: script) {
            apple.executeAndReturnError(&error)
            if let e = error {
                print("AppleScript error: \(e)")
            }
        }
    }
}
