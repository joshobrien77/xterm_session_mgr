# config.py

"""
Module for loading iTerm2 session definitions from a JSON file.
Defines the Session dataclass and a loader function.
"""

import json
from dataclasses import dataclass
from typing import List, Optional

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

    The JSON file should contain an array of objects with keys:
      - id           (str)   : unique identifier
      - name         (str)   : display name
      - host         (str)   : hostname or IP
      - port         (int)   : SSH port (defaults to 22 if omitted)
      - user         (str)   : SSH username
      - identityFile (str)   : path to private key file (optional)
      - launchMode   (str)   : "newWindow", "newTab", or "splitPane"
      - passwordKey  (str)   : Keychain key for stored password (optional)

    Returns:
        List[Session]: a list of Session instances.
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
