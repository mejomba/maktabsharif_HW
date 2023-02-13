import sqlite3
from typing import Tuple
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "metro.db")


def create_db():
    # if we error, we rollback automatically, else commit!
    with sqlite3.connect('testDB.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT SQLITE_VERSION()')
        data = cursor.fetchone()
        print('SQLite version:', data)


# def create_table(table_name, fields: Tuple):
def create_table(table_name, kwargs):
    with sqlite3.connect('testDB.db') as conn:
        cur = conn.cursor()
        print(kwargs)
        # query = "CREATE TABLE IF NOT EXISTS {0} ({1});".format(table_name, fields)
        query = "CREATE TABLE IF NOT EXISTS person (:id, :first_name, :last_name);"
        print(query)
        cur.execute(query, kwargs)
        # data = cur.execute("CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(50), last_name VARCHAR(50));")
        # cursor.execute("INSERT INTO table VALUES ?", args)


def insert_query(*args, **kwargs):
    with sqlite3.connect('testDB.db') as conn:
        cur = conn.cursor()
        print(kwargs)
        query = "INSERT INTO person (first_name, last_name) VALUES (:first_name, :last_name)"
        cur.execute(query, kwargs)
        conn.commit()
        # cursor.execute("INSERT INTO table VALUES ?", args)


def select_query(*args, **kwargs):
    with sqlite3.connect('testDB.db') as conn:
        cur = conn.cursor()
        print(args)
        query = "SELECT * FROM person where first_name=(:first_name)"
        # query = "SELECT * FROM person where first_name='%s'" % kwargs['first_name']
        print(query)
        cur.execute(query, kwargs)
        data = cur.fetchall()
        print(data)
        # cursor.execute("INSERT INTO table VALUES ?", args)


# create_table('person', {'id':'INTEGER PRIMARY KEY AUTOINCREMENT', 'first_name':'VARCHAR(50)', 'last_name':'VARCHAR(50)'})
# create_table()
# insert_query(first_name="zahra", last_name='jafari')
# select_query(first_name="zahra")
# select_query(first_name="' OR 1; --")

with sqlite3.connect(db_path) as con:
    print(db_path)
    cur = con.cursor()
    query = """
    INSERT INTO user (
                    first_name, 
                    last_name, 
                    password, 
                    phone, 
                    email, 
                    role_id, 
                    is_authenticated, 
                    have_bank_account) VALUES ('mojtaba','aminzadeh','12345','0936','email','1',0,0);
                    """
    data = ('mojtaba','aminzadeh','12345','0936','email','1',0,0)
    cur.execute("SELECT * FROM user;")
    # cur.execute(".help")








