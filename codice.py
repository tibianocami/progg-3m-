import json
import random

USERS_FILE = "users.json"

# ----------------------------
# WORDLIST stile Bitcoin (semplificata)
# ----------------------------
WORDLIST = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb",
    "abstract", "absurd", "abuse", "access", "accident", "account",
    "accuse", "achieve", "acid", "acoustic", "acquire", "across",
    "act", "action", "actor", "actual", "adapt", "add", "address",
    "adjust", "adult", "advance", "advice", "aerobic"
]

# ----------------------------
# LOAD / SAVE JSON
# ----------------------------
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ----------------------------
# UTIL
# ----------------------------
def generate_code():
    return str(random.randint(100000, 999999))

def generate_seed_password():
    return " ".join(random.choice(WORDLIST) for _ in range(12))

def valid_email(email):
    return "@" in email and "." in email

# ----------------------------
# REGISTRAZIONE
# ----------------------------
def create_account(users):
    username = input("Inserisci username: ")

    if username in users:
        print("❌ Username già esistente")
        return None

    email = input("Inserisci email: ")

    if not valid_email(email):
        print("❌ Email non valida")
        return None

    code = generate_code()
    print(f"\n📩 Codice inviato (simulazione): {code}")

    user_code = input("Inserisci codice ricevuto: ")

    if user_code != code:
        print("❌ Codice errato")
        return None

    password = generate_seed_password()

    print("\n🔐 SEED PASSWORD (SALVALA SUBITO!)")
    print(password)

    users[username] = {
        "email": email,
        "password": password
    }

    save_users(users)
    print("✅ Account creato con successo")

    return username

# ----------------------------
# LOGIN
# ----------------------------
def login(users):
    username = input("Username: ")
    password = input("Password seed: ")

    if username in users and users[username]["password"] == password:
        print("✅ Login effettuato")
        return username

    print("❌ Credenziali errate")
    return None

# ----------------------------
# MENU UTENTE
# ----------------------------
def user_menu(users, username):
    while True:
        print("\n--- MENU UTENTE ---")
        print("1. Modifica username")
        print("2. Mostra password seed")
        print("3. Logout")

        choice = input("> ")

        if choice == "1":
            new_username = input("Nuovo username: ")

            if new_username in users:
                print("❌ Username già esistente")
            else:
                users[new_username] = users.pop(username)
                username = new_username
                save_users(users)
                print("✅ Username aggiornato")

        elif choice == "2":
            print("🔐", users[username]["password"])

        elif choice == "3":
            print("👋 Logout...")
            break

# ----------------------------
# MAIN APP
# ----------------------------
def main():
    users = load_users()

    while True:
        print("\n=== APP PRINCIPALE ===")
        print("1. Login")
        print("2. Crea account")
        print("3. Esci")

        choice = input("> ")

        if choice == "1":
            user = login(users)
            if user:
                user_menu(users, user)

        elif choice == "2":
            user = create_account(users)
            if user:
                user_menu(users, user)

        elif choice == "3":
            print("🚪 Uscita app")
            break

if __name__ == "__main__":
    main()