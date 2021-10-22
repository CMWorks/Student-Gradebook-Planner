class Authentication:
    def __init__(self, db):
        raise NotImplementedError

    def register(email, userID):
        raise NotImplementedError

    def login(self, email: str, userID: str):
        raise NotImplementedError

    def verify(token):
        raise NotImplementedError
