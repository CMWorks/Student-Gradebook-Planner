from auth.jwtAuth import JWTAuth
from database.SQLQuery import SQLQuery
from obj.User import User
from obj.UserDbHandler import UserDbHandler
import pytest

# Command: python -m pytest -v

db = SQLQuery.getDbQuery("serverTest.txt")
auth = JWTAuth(db)

def user_data():
    user_dict = {
        'userID': "azasfdsafasdfa;",
        'firstName': 'Chris',
        'lastName': 'Moore',
        'email': "test@ilstu.edu",
        'totalGPA': 6.0
    }
    return user_dict

def setup():
    clean()
    user_dict = user_data()
    user = User(user_dict)
    UserDbHandler.add(db, user)
    db.add('CREDENTIALS', {'userID': user.userID, 'email': user.email})
    return user


def clean():
    db.delete('CREDENTIALS', 'userID', 'azasfdsafasdfa;')
    UserDbHandler.delete(db, 'userID', 'azasfdsafasdfa;')

#########################
# Inputing data correctly
#########################

def test_register_standard_newToken():
    clean()
    user = User(user_data())
    added = UserDbHandler.add(db, user)
    token = auth.register(user.email+"Hashed", user.userID)
    verified = auth.verify(token)
    clean()
    
    assert verified and token is not False and added
    
def test_register_invalid_keyError():
    clean()
    data = user_data()
    data.popitem()
    with pytest.raises(KeyError) as exc_info:
        user = User(data)
        
    clean()
    
    exception_raised = exc_info.value
    assert exception_raised
    
def test_register_duplicate_false():
    setup()
    data = user_data()
    user = User(data)
    token = auth.register(user.email, user.userID)
    clean()
    
    assert token is False
    
    
def test_authenticate_standard_newToken():
    setup()
    user = User(user_data())
    token = auth.login(user.email, user.userID)
    verified = auth.verify(token)
    clean()
    
    assert verified and token is not False
    
def test_authenticate_wrongCredentials_false():
    setup()
    user = User(user_data())
    token = auth.login(user.email+"-", user.userID)
    clean()
    
    assert token is False
    