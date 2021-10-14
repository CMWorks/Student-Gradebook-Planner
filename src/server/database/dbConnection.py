class DbConnection:
    def __init__(self):
        raise NotImplementedError
    
    def connect(self, path):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError