from infrastructure.mongo import db

def register_user(name: str, email:str, password_hash: str):
    # first check if the user already exists
    existing_user = db.users.find({"email": email})
    print(existing_user)


register_user("Gabriel", "my@email.com", "pass")