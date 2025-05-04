# tests/test_keychain.py

import keychain
import pytest

def test_keychain_store_and_retrieve(monkeypatch):
    # In-memory fake store
    store = {}

    def fake_set(service, key, password):
        store[(service, key)] = password

    def fake_get(service, key):
        return store.get((service, key), None)

    # Monkeypatch keyring calls in our module
    monkeypatch.setattr(keychain.keyring, "set_password", fake_set)
    monkeypatch.setattr(keychain.keyring, "get_password", fake_get)

    # Save and retrieve
    keychain.save_password("host1", "pass1")
    assert keychain.get_password("host1") == "pass1"
    # Unknown key should return None
    assert keychain.get_password("does-not-exist") is None
