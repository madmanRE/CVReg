from database.db_init import start as create_table
from database.db_manager import add_user, del_user
from auth.hashing_password import hash_password
from auth.auth_module import check_user
from cvc.make_photo import make_profile_photo


def create_table_for_start():
    create_table()


def create_user(
    username: str = None,
    hashedpassword: str = None,
    email: str = None,
    photo: str = None,
    fake: bool = False,
):
    try:
        if fake:
            fake_user = {
                "username": "roma",
                "hashedpassword": "password",
                "email": "test@mail.com",
                "photo": "png",
            }

            add_user(**fake_user)
        else:
            photo = make_profile_photo(f"{email}")
            new_user = {
                "username": username,
                "hashedpassword": hashedpassword,
                "email": email,
                "photo": photo,
            }
            add_user(**new_user)
    except Exception as e:
        return {"error": f"{e}"}


def delete_user(username, password):
    return del_user(username, password)


def check_auth(username, password):
    return check_user(username, password)
