from lib.user import *


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        existing_username = self._connection.execute('SELECT * FROM users WHERE username = %s', [user.username])
        existing_email_address = self._connection.execute('SELECT * FROM users WHERE email_address = %s', [user.email_address])
        if existing_username:
            raise Exception("Username taken.")
        existing_email_address = self._connection.execute('SELECT * FROM users WHERE email_address = %s', [user.email_address])
        if existing_email_address:
            raise Exception("Account already exists, please log in.")
        elif "@" not in user.email_address:
            raise Exception("Invalid email address.")
        self._connection.execute(
            'INSERT INTO users (email_address, username, password) VALUES (%s, %s, %s)', [user.email_address, user.username, user.password])
        return None
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        result = []
        for row in rows:
            item = User(row['id'], row['email_address'], row['username'], row['password'])
            result.append(item)
        return result
    
    def find_by_username(self, username):
        rows = self._connection.execute('SELECT id, email_address, username, password FROM users WHERE username = %s', (username,))
        row = rows[0]
        return User(row['id'], row['email_address'], row['username'], row['password'])  