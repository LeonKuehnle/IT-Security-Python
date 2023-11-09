import pytest
import sqlite3
from example1 import login

# Hier sollten "your_code_file" durch den Dateinamen ersetzt werden, in dem sich der Python-Code befindet.

# Einrichten der Testdatenbank und Nutzer
def setup_module(module):
    conn = sqlite3.connect("test_users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('testuser', 'testpassword')")
    conn.commit()
    conn.close()

# Aufräumen nach den Tests
def teardown_module(module):
    conn = sqlite3.connect("test_users.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    conn.close()

# Testfälle
def test_successful_login():
    assert login("testuser", "testpassword") == "Erfolgreich eingeloggt!"

def test_failed_login():
    assert login("nonexistentuser", "wrongpassword") == "Fehler beim Einloggen!"

def test_sql_injection():
    # Übergeben von SQL-Injections als Benutzername und Passwort sollte immer fehlschlagen
    assert login("'; DROP TABLE users --", "'; DROP TABLE users --") == "Fehler beim Einloggen!"

def test_empty_input():
    assert login("", "") == "Fehler beim Einloggen!"