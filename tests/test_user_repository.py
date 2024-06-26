from lib.user import User
from lib.user_repository import UserRepository

def test_create(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = UserRepository(db_connection)
    new_user = User(5, 'olikelly1234@gmail.com', 'olikelly1234', 'password5')

    repo.create(new_user)
    assert repo.all() == [
        User(1, 'Joe1234@gmail.com', 'Joe1234', 'password1'),
        User(2, 'Anna1234@gmail.com', 'Anna1234', 'password2'),
        User(3, 'Joseph5678@hotmail.com', 'Joseph5678', 'password3'),
        User(4, 'Sophie1234@outlook.com', 'Sophie1234', 'password4'),
        User(5, 'olikelly1234@gmail.com', 'olikelly1234', 'password5')
        ]
    
def test_find_by_username(db_connection):
    db_connection.seed('../seeds/seeds_words.sql')
    repo = UserRepository(db_connection)
    assert repo.find_by_username('Joe1234') == User(1, 'Joe1234@gmail.com', 'Joe1234', 'password1')
    assert repo.find_by_username('Sophie1234') == User(4, 'Sophie1234@outlook.com', 'Sophie1234', 'password4')
