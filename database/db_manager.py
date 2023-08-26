from database.db_connect import add_u, delete_u


def add_user(username: str, hashedpassword: str, email: str, photo: str):
    try:
        result = add_u(username, hashedpassword, email, photo)
        return result
    except Exception as e:
        return {"error": f"{e}"}


def del_user(username: str, password: str):
    try:
        return delete_u(username, password)
    except Exception as e:
        return {"message": f"{e}"}
