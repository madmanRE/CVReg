from database.db_connect import get_user
from auth.hashing_password import hash_password
from cvc import core, make_photo


def check_user(username, password):
    try:
        user = get_user(username, hash_password(password))
        if user != "No user found":
            current_photo = make_photo.make_profile_photo(user[3], 2)
            if core.compare(user[4], current_photo) == True:
                return {"status": 200, "message": "authorization passed"}
            else:
                return {"status": 403, "message": "authorization canceled (photo)"}
        else:
            return {"status": 403, "message": "authorization canceled (user)"}
    except Exception as e:
        return {"error": f"{e}"}
