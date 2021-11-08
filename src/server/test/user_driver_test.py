from obj.User import User
from obj.UserDbHandler import UserDbHandler
from database.SQLQuery import SQLQuery
import pytest

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")


#########################
# Helpful Funcitons
#########################

def setup():
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


def test_userHandler_get_standard_user():
    # setup
    user = setup()

    # test
    dbUser = UserDbHandler.get(db, 'userID', user.getUserID())
    assert user.toJson() == dbUser.toJson()

    # cleanup
    cleanup()


def test_userHandler_get_wrongID_None():
    # setup
    setup()

    # test
    dbUser = UserDbHandler.get(db, 'userID', 0)
    assert dbUser == None

    # cleanup
    cleanup()


def test_userHandler_get_notInDatabase_None():
    cleanup()
    # test
    data = user_data()
    dbUser = UserDbHandler.get(db, 'userID', data['userID'])
    assert dbUser == None


def test_userHandler_get_noDB_None():
    cleanup()
    # test
    data = user_data()
    dbUser = UserDbHandler.get(None, 'userID', data['userID'])
    assert dbUser == None


def test_userHandler_delete_standard_true():
    # setup
    user = setup()

    # test
    success = UserDbHandler.delete(db, 'userID', user.getUserID())
    assert success == True

    # cleanup
    cleanup()


def test_userHandler_delete_wrongID_false():
    # setup
    setup()

    # test
    success = UserDbHandler.delete(db, 'userID', 0)
    assert success == False

    # cleanup
    cleanup()


def test_userHandler_delete_notInDatabase_false():
    cleanup()
    # test
    data = user_data()
    success = UserDbHandler.delete(db, 'userID', data['userID'])
    assert success == False


def test_userHandler_delete_noDB_false():
    # test
    data = user_data()
    success = UserDbHandler.delete(None, 'userID', data['userID'])
    assert success == False


def test_userHandler_add_standard_true():
    cleanup()
    data = user_data()
    user = User(data)

    # test
    success = UserDbHandler.add(db, user)
    assert success == True

    # cleanup
    cleanup()


def test_userHandler_add_noUser_false():
    # test
    success = UserDbHandler.add(db, None)
    assert success == False

    # cleanup
    cleanup()


def test_userHandler_add_userAlreadyExist_false():
    # setup
    user = setup()

    # test
    success = UserDbHandler.add(db, user)
    assert success == False

    # cleanup
    cleanup()


def test_userHandler_add_duplicateID_false():
    # setup
    user = setup()

    # test
    user.setFirstName('')
    user.setLastName('')
    user.setEmail('')
    user.setTotalGPA(0)
    success = UserDbHandler.add(db, user)
    assert success == False

    # cleanup
    cleanup()


def test_userHandler_update_standard_true():
    user = setup()
    user.setFirstName('_Test_')

    # test
    success = UserDbHandler.update(db, user)
    assert success == True

    # cleanup
    cleanup()


def test_userHandler_update_get_standard_updatedUser():
    user = setup()
    user.setFirstName('_Test_')

    # test
    success = UserDbHandler.update(db, user)
    dbUser = UserDbHandler.get(db, 'userID', user.getUserID())
    assert user.toJson() == dbUser.toJson() and success

    # cleanup
    cleanup()


def test_userHandler_update_noUser_false():
    # test
    success = UserDbHandler.update(db, None)
    assert success == False

    # cleanup
    cleanup()


def test_userHandler_update_userAlreadyExist_true():
    # setup
    user = setup()

    # test
    success = UserDbHandler.update(db, user)
    assert success == True

    # cleanup
    cleanup()

def test_userHandler_cleanup():
    cleanup()
    assert True