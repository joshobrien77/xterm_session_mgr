import Foundation

class SessionStore: ObservableObject {
    @Published var sessions: [Session] = []

    func load(from path: String? = nil) {
        let url = URL(fileURLWithPath:
            path ?? (NSHomeDirectory() + "/.iterm2_sessions.json")
        )
        do {
            let data = try Data(contentsOf: url)
            sessions = try JSONDecoder().decode([Session].self, from: data)
        } catch {
            print("Failed to load sessions:", error)
        }
    }
}
