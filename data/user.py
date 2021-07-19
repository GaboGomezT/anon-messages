from infrastructure.mongo import db
from passlib.handlers.sha2_crypt import sha512_crypt as crypto

def register_user(name: str, email:str, password: str):
    # first check if the user already exists
    existing_user = db.users.find({"email": email}).count()
    if existing_user != 0:
        print("ya existe esta correo")
        return "Este correo ya existe"
    
    db.users.insert_one({
        "name": name,
        "email": email,
        "password_hash": crypto.hash(password, rounds=172_434)
    })
    return None


def login_user(email:str, password: str):
    # first check if the user already exists
    existing_user = db.users.find({"email": email})
    if existing_user.count() == 0:
        print("este usuario no existe")
        return "Este correo no existe"
    
    if not crypto.verify(password, existing_user.next()["password_hash"]):
        print("contraseña incorrecta")
        return "Wrong password"
    return None


