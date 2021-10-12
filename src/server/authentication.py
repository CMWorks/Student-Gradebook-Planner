import jwt
import time


class Authentication:
    def __init__(self):
        self.__validation_time_hours = 24
        self.__key = "42"

    def createAuthToken(self, email, userID):
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

    def checkAuthToken(self, authToken):
        try:
            payload = jwt.decode(authToken, self.__key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError as error:
            print(f'Expired token: {error}')
            return False
        except jwt.InvalidSignatureError as error:
            print(f'Invalid token: {error}')
            return False
