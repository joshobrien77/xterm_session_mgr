import json
from pathlib import Path

def load_sessions(path: str = None):
    """Load sessions JSON from the given path or default file."""
    path = Path(path or Path.home() / ".iterm2_sessions.json")
    return json.loads(path.read_text())
