from obj.User import User
from obj.UserDbHandler import UserDbHandler
from database.SQLQuery import SQLQuery
import pytest

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")


#########################
# Helpful Funcitons
#########################

def setup() -> User:
    cleanup()
    user_dict = {
        'userID': "azasfdsafasdfa",
        'firstName': 'Chris',
        'lastName': 'Moore',
        'email': "test@ilstu.edu",
        'totalGPA': 6.0
    }
    db.add('STUDENT', user_dict)
    user = User(user_dict)
    return user


def cleanup():
    db.delete('STUDENT', 'userID', 'azasfdsafasdfa')


def user_data():
    user_dict = {
        'userID': "azasfdsafasdfa",
        'firstName': 'Chris',
        'lastName': 'Moore',
        'email': "test@ilstu.edu",
        'totalGPA': 6.0
    }
    return user_dict

#########################
# Inputing data correctly
#########################
def test_editAccount_correctData_true():
    user = setup()
    
    user.setFirstName("__new__")
    
    success = UserDbHandler.update(db, user)
    new_user = UserDbHandler.get(db, "userID", user.userID)
    
    cleanup()
    
    assert success and user.toJson() == new_user.toJson()
    
def test_editAccount_invalidData_KeyError():
    setup()
    
    with pytest.raises(KeyError) as exc_info:
        user = User({})
        
    cleanup()
        
    exception_raised = exc_info.value
    assert exception_raised
    

def test_deleteAccount_correctID_true():
    user = setup()
    
    success = UserDbHandler.delete(db, "userID", user.userID)
    new_user = UserDbHandler.get(db, "userID", user.userID)
    
    cleanup()
    
    assert success and new_user == None
    
def test_deleteAccount_invalidID_false():
    user = setup()
    
    success = UserDbHandler.delete(db, "userID", "")
    new_user = UserDbHandler.get(db, "userID", user.userID)
    
    cleanup()
    
    assert not success and new_user.toJson() == user.toJson()
    

def test_cleanup():
    cleanup()
    assert True