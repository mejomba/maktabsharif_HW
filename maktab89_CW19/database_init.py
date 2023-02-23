import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def database_connect(db_name):
    conn = psycopg2.connect(database=db_name, user='postgres', password='093605216888', port=5434)
    cur = conn.cursor()
    return conn, cur


def __create_database():
    conn = psycopg2.connect(database='postgres', user='postgres', password='093605216888', port=5434)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    db_name = 'blog'
    cur.execute('CREATE DATABASE ' + db_name + ';')
    conn.commit()
    cur.close()
    conn.close()


def __create_tables():
    query = """ CREATE TABLE IF NOT EXIST users
            (user_id serial primary key, 
            username varchar(50) unique not null, 
            password varchar(100) not null, 
            created_at timestamptz not null default NOW()
            );"""
    conn, cur = database_connect('blog')
    cur.execute(query)
    conn.commit()

    query = """
            CREATE TABLE IF NOT EXIST posts (
            post_id serial primary key,
            user_id integer ,
            title varchar(50) not null,
            body text not null,
            created_at timestamptz not null default NOW(),
            CONSTRAINT FK_posts_users FOREIGN KEY(user_id)
            REFERENCES users(user_id)
            );
            """
    cur.execute(query)
    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    __create_database()
    __create_tables()