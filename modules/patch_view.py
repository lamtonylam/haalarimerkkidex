"""
This module is used for the template patch_view.html.
"""

from sqlalchemy.sql import text
from db import db
from flask import flash


def get_patch_name(id):
    # Fetch patch name of the patch
    query_patch = text("SELECT name FROM Patches WHERE id = :id;")
    result_patch = db.session.execute(query_patch, {"id": id})
    row = result_patch.fetchone()
    patch_name = row[0]
    return patch_name


def get_created_by_user(id):
    # Fetch username of the patch
    sql = text(
        """SELECT users.username 
        FROM users, patches 
        WHERE patches.id = :id 
        AND patches.created_by_user = users.id"""
    )

    created_by_user = db.session.execute(sql, {"id": id})
    created_by_user = created_by_user.fetchone()[0]

    return created_by_user


def get_image(id):
    # Fetch image data
    query_image = text("SELECT data FROM Patches WHERE id=:patch_id")
    result_image = db.session.execute(query_image, {"patch_id": id})

    return result_image


def get_comments(id):
    # Fetch comments of the patch
    sql = text(
        """SELECT comments.comment, comments.sent_at, users.username 
        FROM comments, users 
        WHERE patch_id = :patch_id 
        AND comments.user_id = users.id"""
    )
    result_comments = db.session.execute(sql, {"patch_id": id})
    comments = result_comments.fetchall()

    list_comments = []
    for comment in comments:
        list_comments.append((comment[0], comment[1], comment[2]))

    return list_comments


def get_category(id):
    sql = text(
        "SELECT Categories.name FROM Categories, Patches WHERE Patches.category_id = Categories.id AND Patches.id = :id"
    )
    result = db.session.execute(sql, {"id": id})
    category = result.fetchone()[0]
    return category


def patch_into_collection(patch_id, user_id):
    sql_set_timezone = text("SET TIME ZONE 'Europe/Helsinki';")
    db.session.execute(sql_set_timezone)
    try:
        sql = text(
            "INSERT INTO UsersToPatches (patch_id, user_id, sent_at) VALUES (:patch_id, :user_id, NOW())"
        )
        db.session.execute(sql, {"patch_id": patch_id, "user_id": user_id})
        db.session.commit()
    except Exception as e:
        print(e)
        return False

    return True


def add_comment(patch_id, user_id, comment):
    sql_set_timezone = text("SET TIME ZONE 'Europe/Helsinki';")
    db.session.execute(sql_set_timezone)
    try:
        sql = text(
            """INSERT INTO Comments (patch_id, user_id, comment, sent_at) 
            VALUES (:patch_id, :user_id, :comment, NOW())"""
        )
        db.session.execute(
            sql, {"patch_id": patch_id, "user_id": user_id, "comment": comment}
        )
        db.session.commit()
        flash("Kommentti lisätty onnistuneesti!", "success")
    except Exception as e:
        print(e)
        flash("Kommentin lisääminen epäonnistui!", "error")


# delete a patch from general collection
def delete_patch(patch_id):
    sql = text("DELETE FROM Patches WHERE id = :patch_id")
    db.session.execute(sql, {"patch_id": patch_id})
    db.session.commit()


# delete a patch from user's collection
def delete_patch_from_collection(patch_id, user_id):
    sql = text(
        "DELETE FROM UsersToPatches WHERE patch_id = :patch_id AND user_id = :user_id"
    )
    db.session.execute(sql, {"patch_id": patch_id, "user_id": user_id})
    db.session.commit()
