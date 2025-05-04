from applescript import build_applescript

def test_build_applescript_new_window():
    sess = { "name": "X", "host": "h", "user": "u", "identityFile": "/key", "launchMode": "newWindow" }
    script = build_applescript(sess)
    assert "create window" in script
    assert "ssh -i \"/key\" u@h" in script

def test_build_applescript_new_tab():
    sess = { "name": "X", "host": "h", "user": "u", "identityFile": "", "launchMode": "newTab" }
    script = build_applescript(sess)
    assert "create tab" in script
    assert "ssh -i \"\" u@h" in script
