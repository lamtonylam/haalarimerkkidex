from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text
import secrets


def login(username, password):
    sql = text("SELECT id, password, username FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False


def logout():
    try:
        del session["username"]
    except Exception as e:
        print(e)
        pass
    try:
        del session["user_id"]
    except Exception as e:
        print(e)
        pass


def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text(
            "INSERT INTO users (username, password) VALUES (:username, :password)"
        )
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
    except Exception as e:
        print(e)
        return False
    return login(username, password)


def user_id():
    return session.get("user_id", 0)


def get_username():
    return session.get("username", "")