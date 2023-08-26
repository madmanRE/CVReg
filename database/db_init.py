from database.db_connect import create_table


def start():
    try:
        create_table()
        return {"message": "database has been created"}
    except Exception as e:
        return {"message": f"{e}"}
