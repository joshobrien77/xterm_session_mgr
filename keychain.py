# keychain.py

import keyring
from typing import Optional

# Consistent service name for all sessions
SERVICE_NAME = "iterm2-session-manager"

def save_password(key: str, password: str) -> None:
    """
    Save `password` in the macOS Keychain under SERVICE_NAME and `key`.
    """
    keyring.set_password(SERVICE_NAME, key, password)

def get_password(key: str) -> Optional[str]:
    """
    Retrieve the password stored under SERVICE_NAME and `key`.
    Returns None if no entry exists.
    """
    return keyring.get_password(SERVICE_NAME, key)
