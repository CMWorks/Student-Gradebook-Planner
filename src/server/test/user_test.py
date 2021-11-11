from obj.User import User
import pytest

# Command: python -m pytest -v


def setup():
    user_dict = {
        'userID': "azasfdsafasdfa;",
        'firstName': 'Chris',
        'lastName': 'Moore',
        'email': "test@ilstu.edu",
        'totalGPA': 6.0
    }
    return user_dict


def emptySetup():
    user_dict = {
        'userID': '',
        'firstName': '',
        'lastName': '',
        'email': '',
        'totalGPA': 0.0
    }
    return user_dict

#########################
# Inputing data correctly
#########################

def test_user_standard_nothing():
    data = setup()
    user = User(data)
    assert user.toJson() == setup()
    del user


def test_user_noData_KeyError():
    with pytest.raises(KeyError) as exc_info:
        user = User({})

    exception_raised = exc_info.value
    assert exception_raised


def test_user_incorrectType_TypeError():
    data = setup()
    data['userID'] = 0
    with pytest.raises(TypeError) as exc_info:
        user = User(data)

    exception_raised = exc_info.value
    assert exception_raised


def test_user_function_TypeError():
    data = setup
    with pytest.raises(TypeError) as exc_info:
        user = User(data)

    exception_raised = exc_info.value
    assert exception_raised


def test_user_functionVariable_TypeError():
    data = setup()
    data['userID'] = setup
    with pytest.raises(TypeError) as exc_info:
        user = User(data)

    exception_raised = exc_info.value
    assert exception_raised


def test_user_array_TypeError():
    with pytest.raises(TypeError) as exc_info:
        user = User([])

    exception_raised = exc_info.value
    assert exception_raised


def test_user_null_TypeError():
    with pytest.raises(TypeError) as exc_info:
        user = User(None)

    exception_raised = exc_info.value
    assert exception_raised


def test_user_objectInObject_TypeError():
    data = setup()
    with pytest.raises(TypeError) as exc_info:
        user = User({data})

    exception_raised = exc_info.value
    assert exception_raised
