from obj.User import User
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

def test_delete_standard_true():
    # setup
    user = setup()

    # test
    success = db.delete('STUDENT', 'userID', user.getUserID())
    assert success == True

    # cleanup
    cleanup()


def test_delete_wrongID_false():
    # setup
    setup()

    # test
    success = db.delete('STUDENT', 'userID', 0)
    assert success == False

    # cleanup
    cleanup()


def test_delete_notInDatabase_false():
    cleanup()
    # test
    data = user_data()
    success = db.delete('STUDENT', 'userID', data['userID'])
    assert success == False


def test_delete_noTable_false():
    # test
    data = user_data()
    success = db.delete("", 'userID', data['userID'])
    assert success == False


def test_add_standard_true():
    cleanup()
    data = user_data()

    # test
    success = db.add('STUDENT', data)
    assert success == True

    # cleanup
    cleanup()


def test_add_noTable_false():
    cleanup()
    data = user_data()
    
    # test
    success = db.add('', data)
    assert success == False

    # cleanup
    cleanup()


def test_add_alreadyExist_false():
    # setup
    user = setup()

    # test
    success = db.add('STUDENT', user.toJson())
    assert success == False

    # cleanup
    cleanup()


def test_add_noData_false():
    # setup
    cleanup()

    # test
    success = db.add('STUDENT', {})
    assert success == False

    # cleanup
    cleanup()


def test_update_standard_true():
    user = setup()
    user.setFirstName('_Test_')

    # test
    success = db.update('STUDENT', user.toJson(), 'userID', user.userID)
    assert success == True

    # cleanup
    cleanup()


def test_update_noTable_false():
    user = setup()
    user.setFirstName('_Test_')

    # test
    success = db.update('', user.toJson(), 'userID', user.userID)
    assert success == False

    # cleanup
    cleanup()


def test_update_noData_false():
    user = setup()
    user.setFirstName('_Test_')
    
    # test
    success = db.update('STUDENT', {}, 'userID', user.userID)
    assert success == False

    # cleanup
    cleanup()

def test_cleanup():
    cleanup()
    assert True