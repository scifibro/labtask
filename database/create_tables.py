from commands import create_tables
import db
from execute_query import execute_q
from db import db_error


if __name__ == '__main__':
    execute_q(conn=db.conn, commands=create_tables, db_error=db_error)

