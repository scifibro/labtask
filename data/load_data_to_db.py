import os

from database import db
from database.db import db_error


files_and_commands = {}


for root, dirs, files in os.walk(os.path.abspath("/data/csv")):
    for file in files:
        files_and_commands[f'{os.path.join(root, file)}'] = f"COPY {file[:-4]} FROM STDIN DELIMITER ',' CSV HEADER"


def write_csv_to_db(conn, files_and_commands, db_error):
    """
    write csv data to database tables
    :param conn: database connection
    :param files_and_commands: dict with file path as keys,values - tablename(tablename and filename must be same
    :param db_error: error handler
    :return: none
    """
    db_conn = None
    try:
        db_conn = conn
        cur = db_conn.cursor()
        for file, sql in files_and_commands.items():
            cur.copy_expert(sql, open(file, "r"))
        cur.close()
        db_conn.commit()
    except (Exception, db_error) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()


if __name__ == '__main__':
    write_csv_to_db(conn=db.conn, files_and_commands=files_and_commands, db_error=db_error)

