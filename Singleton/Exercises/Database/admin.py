from database_conf import Database

def add_user(username, role):
    db = Database()  # should always get same instance
    db.add_user(username, role)
    print(f"User '{username}' added.")

def show_user(username):
    db = Database()
    user = db.get_user(username)
    if user:
        print(f"{username} → {user}")
    else:
        print("User not found.")

def show_all_users():
    db = Database()
    users = db.list_users()
    print("All Users:")
    for u in users:
        print(u)
