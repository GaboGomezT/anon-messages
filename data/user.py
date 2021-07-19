from infrastructure.mongo import db

def register_user(name: str, email:str, password_hash: str):
    # first check if the user already exists
    existing_user = db.users.find({"email": email}).count()
    if existing_user != 0:
        print("ya existe esta correo")
        return "Este correo ya existe"
    
    db.users.insert_one({
        "name": name,
        "email": email,
        "password_hash": password_hash
    })
    return None


