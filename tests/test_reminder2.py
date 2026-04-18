import pytest # <-- New code
from lib.reminder2 import *


def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"


"""
There are three key differences:

We import pytest so we can use it to check for errors.
We use with pytest.raises(Exception) as e: to set up a section of the code where we expect an error to happen and then be caught by pytest.
We use str(e.value) to get the error message that was generated, and then assert that it is the correct one.
"""