import json
import hashlib
import os

DATA_FILE = 'users.json'

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(users):
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter new password: ")
    users[username] = {
        'password': hash_password(password),
        'login_count': 0
    }
    save_users(users)
    print("Account created successfully!")

def login(users):
    username = input("Enter username: ")
    if username not in users:
        print("User not found.")
        return
    password = input("Enter password: ")
    if users[username]['password'] == hash_password(password):
        users[username]['login_count'] += 1
        save_users(users)
        print(f"Welcome back, {username}!")
        print(f"Login count: {users[username]['login_count']}")
    else:
        print("Incorrect password.")

def view_all_users(users):
    print("\n--- Registered Users ---")
    for user, info in users.items():
        print(f"Username: {user}, Logins: {info['login_count']}")
    print("------------------------\n")

def main():
    users = load_users()
    while True:
        print("\n1. Sign Up\n2. Login\n3. View All Users (admin)\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            signup(users)
        elif choice == '2':
            login(users)
        elif choice == '3':
            view_all_users(users)
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if name == 'main':
    main()