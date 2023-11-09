def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        return "Erfolgreich eingeloggt!"
    else:
        return "Fehler beim Einloggen!"

if __name__ == "__main__":
    # Simulieren von Benutzereingaben mit Dummy-Daten
    username = "testuser"
    password = "testpassword"
    result = login(username, password)
    print(result)
