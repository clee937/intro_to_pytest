from lib.check_codeword import *

"""
If the codeword is correct, returns 'Correct! Come in.'
"""
def test_with_with_correct_codeword():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

"""
If the codeword is has the right first and last letter, returns 'Close, but nope.'
"""
def test_with_partially_correct_codeword():
    result = check_codeword('hare')
    assert result == 'Close, but nope.'

"""
If the codeword is has the right first and the wrong last letter, returns 'WRONG!'
"""

def test_with_right_first_letter_and_wrong_first_letter():
    result = check_codeword('hat')
    assert result == 'WRONG!', 'testing with hat'

"""
If the codeword is has the wrong first and the right last letter, returns 'WRONG!'
"""

def test_with_wrong_first_letter_and_right_first_letter():
    result = check_codeword('mouse')
    assert result == 'WRONG!', 'testing with mouse'

"""
If the codeword is incorrect, returns 'WRONG!'
"""
def test_with_incorrect_codeword():
    result = check_codeword('panda')
    assert result == 'WRONG!'