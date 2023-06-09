import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_conn():
    """
    - Creates and connects to the postgres
    - Returns the connection and cursor to postgres
    """
    
    # connect to default database
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Tuan03041901")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # close connection to default database
    conn.close()    
    
    # connect to postgres database
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Tuan03041901")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the postgres database. 
    
    - Establishes connection with the postgres database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_conn()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()