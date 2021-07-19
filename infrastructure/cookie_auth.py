import hashlib
from typing import Optional

from fastapi import Request
from fastapi import Response


auth_cookie_name = 'senial_account'


def set_auth(response: Response, email: str):
    hash_val = __hash_text(email)
    val = "{}:{}".format(email, hash_val)
    response.set_cookie(auth_cookie_name, val, secure=False, httponly=True, samesite='Lax')


def __hash_text(text: str) -> str:
    text = 'salty__' + text + '__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_email_via_auth_cookie(request: Request) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    email = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(email)
    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None

    return email


def logout(response: Response):
    response.delete_cookie(auth_cookie_name)
