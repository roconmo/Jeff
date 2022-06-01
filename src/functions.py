#!/usr/bin/env python3
import mysql.connector
from src.sql_queries import create_table_queries, drop_table_queries
from src.config import KEY

def create_database():
    """
    - Creates and connects to the cordis database
    - Returns the cursor to cordis database
    """

    # connect to default database
    conn = mysql.connector.connect(
        host=KEY.get('host'),
        user=KEY.get('user'),
        password=KEY.get('password'),
        auth_plugin="mysql_native_password",
    )

    cur = conn.cursor()
    cur.execute("DROP DATABASE IF EXISTS Jeff_assign")
    cur.execute("CREATE DATABASE Jeff_assign")

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
    Creates each table using the queries in 'create_table_queries' list. 
    Args:
        cur: current cursor
        conn: current connection
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def sql_main():
    """
    - Drop (if exists) and creates the Jeff database. 
    - Establishes connection with the Cordis database and gets cursor to it.  
    - Drops all the tables.  
    - Creates all tables needed. 
    - Finally, closes the connection. 
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    print("Tables created")



