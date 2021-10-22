import jwt
import time
from database.SQLQuery import SQLQuery
from auth.authentication import Authentication


class JWTAuth(Authentication):
    def __init__(self, db: SQLQuery):
        self.__validation_time_hours = 24
        self.__algorithm = "HS256"
        self.__key = "42"
        self.db = db

    def register(self, email: str, userID: str):
        token = self._createAuthToken(email, userID)
        success = self.db.add('Credentials', {'userID':userID, 'email':email})
        if success:
            return token
        else:
            return False

    def login(self, email: str, userID: str):
        isVerified = self._verifyAccount(email, userID)
        if isVerified:
            return self._createAuthToken(email, userID)
        else:
            return False

    def verify(self, token: str):
        return self._checkAuthToken(token)

    def _createAuthToken(self, email, userID):
        payload_data = {
            "exp": int(time.time())+self.__validation_time_hours*3600,
            "email": email,
            "userID": userID
        }

        token = jwt.encode(
            payload=payload_data,
            key=self.__key
        )

        return token

    def _checkAuthToken(self, authToken):
        try:
            payload = jwt.decode(authToken, self.__key,
                                 algorithms=[self.__algorithm])
            return self._verifyAccount(payload['email'], payload['userID'])
        except jwt.ExpiredSignatureError as error:
            print(f'Expired token: {error}')
            return False
        except jwt.InvalidSignatureError as error:
            print(f'Invalid token: {error}')
            return False

    def _verifyAccount(self, email, userID):
        data = self.db.get('Credentials', 'userID', userID)
        found = 0
        for row in data:
            if row[0] == userID and row[1] == email:
                found += 1
        if found == 1:
            return True
        else:
            return False
