from lib.report_length import *

""" Test with the word 'cat'."""

def test_with_a_three_char_word():
    result = report_length('cat')
    assert result == "This string was 3 characters long.", "testing \'cat\'"

""" Test with the word 'mouse'."""

def test_with_a_five_char_word():
    result = report_length('mouse')
    assert result == "This string was 5 characters long.", "testing \'mouse\'"

""" Test with the word 'disproportionateness'."""

def test_with_a_twenty_char_word():
    result = report_length('disproportionateness')
    assert result == "This string was 20 characters long.", "testing \'disproportionateness\'"

""" Test with the an empty string """

def test_with_an_empty_string():
    result = report_length('')
    assert result == "This string was 0 characters long.", "testing with an empty string"

""" Test with the a number """

def test_with_a_number():
    result = report_length(5)
    assert result == "Not a string", "testing with a number"

""" Test with the a boolean """

def test_with_a_boolean():
    result = report_length(True)
    assert result == "Not a string", "testing with a boolean"