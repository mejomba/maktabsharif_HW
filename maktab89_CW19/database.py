from database_init import database_connect


db_name = 'blog'
username = 'postgres'
password = '093605216888'
host = '127.0.0.1'


class UserContextManager:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.err = None
        self.result = None
        self.user = None

    def __enter__(self):
        return self

    def insert_database(self, user):
        self.conn, self.cur = database_connect('blog')
        query = """INSERT INTO users (username, password) VALUES (%s, %s)"""
        data = (user.username, user.password)
        self.cur.execute(query, data)
        self.result = f'user create ....'

    def login(self, username, password):
        self.conn, self.cur = database_connect('blog')
        query = """SELECT * from users where username=(%s) and password=(%s);
                    """
        data = (username, password)
        self.cur.execute(query, data)
        self.user = self.cur.fetchone()
        self.result = 'login success'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.err = f'error: {exc_val}'
            if self.conn and self.cur:
                self.conn.close()
                self.cur.close()
        else:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        return True


class PostContextManager:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.err = None
        self.result = None
        self.posts = None

    def __enter__(self):
        return self

    def insert_to_database(self, post, user_id):
        self.conn, self.cur = database_connect('blog')
        query = """INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s)"""
        data = (user_id, post.title, post.body)
        self.cur.execute(query, data)

    def select_by_user_id(self, user_id):
        self.conn, self.cur = database_connect('blog')
        query = """SELECT * FROM posts WHERE user_id=(%s)"""
        data = (user_id,)
        self.cur.execute(query, data)
        self.posts = self.cur.fetchall()
        self.result = 'fetch success'

    def select_all_post(self):
        self.conn, self.cur = database_connect('blog')
        query = """SELECT * FROM posts"""
        self.cur.execute(query)
        self.posts = self.cur.fetchall()
        self.result = 'fetch success'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.err = f'error: {exc_val}'
            if self.conn and self.cur:
                self.conn.close()
                self.cur.close()
        else:
            self.result = f'post create ....'
            self.conn.commit()
            self.cur.close()
            self.conn.close()
        return True

