from lib.password_checker import *
import pytest

""" When we provide a password with more than 8 characters, True should be returned """
def test_with_valid_password_more_than_8_chars():
    pc = PasswordChecker()
    result = pc.check('123456789')
    assert result == True

""" When we provide a password with exactly 8 characters, True should be returned """
def test_with_valid_8_char_password():
    pc = PasswordChecker()
    result = pc.check('12345678')
    assert result == True

""" When we provide a password with less than 8 characters, an exception is raised"""
def test_with_invalid_7_char_password():
    pc = PasswordChecker()
    with pytest.raises(Exception) as e:
        result = pc.check('1234567')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

