# tests/test_config.py
import json
import tempfile
import pytest
from config import load_sessions, Session

def test_load_sessions(tmp_path):
    sample = [
        {
            "id": "prod-web",
            "name": "Production Web",
            "host": "web01.example.com",
            "port": 2222,
            "user": "deploy",
            "identityFile": "/Users/me/.ssh/id_rsa",
            "launchMode": "newTab",
            "passwordKey": "prod-web@example.com"
        }
    ]
    p = tmp_path / "sessions.json"
    p.write_text(json.dumps(sample))

    sessions = load_sessions(str(p))
    assert len(sessions) == 1
    s = sessions[0]
    assert isinstance(s, Session)
    assert s.id == "prod-web"
    assert s.port == 2222
    assert s.launch_mode == "newTab"
    assert s.identity_file.endswith("id_rsa")
    assert s.password_key == "prod-web@example.com"
