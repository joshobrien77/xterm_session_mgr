import json
import tempfile
from config import load_sessions

def test_load_sessions(tmp_path):
    data = [
        { "name": "Test", "host": "example.com", "user": "u", "identityFile": "", "launchMode": "newTab" }
    ]
    p = tmp_path / "sessions.json"
    p.write_text(json.dumps(data))
    sessions = load_sessions(str(p))
    assert isinstance(sessions, list)
    assert sessions[0]["host"] == "example.com"
