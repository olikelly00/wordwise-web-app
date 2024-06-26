from lib.user import User

def test_user_consructs():
    test_user = User(1, "test_email@email.com", "test_username", "test_password")
    assert test_user.id == 1
    assert test_user.username == "test_username"
    assert test_user.email_address == "test_email@email.com"
    assert test_user.password == "test_password"