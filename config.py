# config.py
from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class Session:
    id: str
    name: str
    host: str
    port: int
    user: str
    identity_file: Optional[str]
    launch_mode: str
    password_key: Optional[str]

def load_sessions(path: str) -> List[Session]:
    """
    Load a list of Session objects from a JSON file at `path`.
    Expects an array of objects with keys:
      - id (str)
      - name (str)
      - host (str)
      - port (int, optional, defaults to 22)
      - user (str)
      - identityFile (str, optional)
      - launchMode (str: 'newWindow'|'newTab'|'splitPane')
      - passwordKey (str, optional)
    """
    with open(path, 'r') as f:
        raw = json.load(f)

    sessions: List[Session] = []
    for entry in raw:
        sessions.append(Session(
            id             = entry['id'],
            name           = entry.get('name', entry['id']),
            host           = entry['host'],
            port           = int(entry.get('port', 22)),
            user           = entry['user'],
            identity_file  = entry.get('identityFile'),
            launch_mode    = entry.get('launchMode', 'newWindow'),
            password_key   = entry.get('passwordKey'),
        ))
    return sessions
