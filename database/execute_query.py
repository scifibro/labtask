def execute_q(conn, commands, db_error):

    """
    execute  any sql query
    Input: database connection, query(str,could be multiple ),errorhandler
    """

    db_conn = None
    try:
        db_conn = conn
        cur = db_conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        db_conn.commit()
    except (Exception, db_error) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()


