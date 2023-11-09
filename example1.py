import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Verwenden Sie benutzereingabe direkt in der SQL-Abfrage, was eine Sicherheitslücke darstellt
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        print("Erfolgreich eingeloggt!")
    else:
        print("Fehler beim Einloggen!")

    conn.close()

if __name__ == "__main__":
    username = input("Benutzername: ")
    password = input("Passwort: ")
    login(username, password)