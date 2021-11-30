from obj.User import User
from database.SQLQuery import SQLQuery
import pytest

# Command: python -m pytest -v
db = SQLQuery.getDbQuery("serverTest.txt")

