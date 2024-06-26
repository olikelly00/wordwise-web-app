class User:
    def __init__(self, id, email_address, username, password):
        self.id = id
        self.email_address = email_address
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__