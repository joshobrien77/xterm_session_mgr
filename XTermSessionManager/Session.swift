import Foundation

struct Session: Identifiable, Codable {
    let id = UUID()
    let name: String
    let host: String
    let user: String
    let identityFile: String?
    let launchMode: String   // "newWindow" or "newTab"
}
