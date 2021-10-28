import db
from db import db_error
from execute_query import execute_q
from commands import create_views


if __name__ == '__main__':
    execute_q(conn=db.conn, commands=create_views, db_error=db_error)