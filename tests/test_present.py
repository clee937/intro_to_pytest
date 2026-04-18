from lib.present import *
import pytest

# Testing for Errors

""" When we wrap an item, we get it back when unwrapping """
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap("Tickle Me Elmo")
    assert present.unwrap() == "Tickle Me Elmo"

""" If we unwrap before unwrapping, we get an error message """
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

""" If we try to wrap an already-wrapped present, we get an error message """
def test_wrapping_already_wrapped_throws_error():
    present = Present()
    present.wrap('lego')
    with pytest.raises(Exception) as e:
        present.wrap('candle')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

""" If we try to wrap an already-wrapped present, the first_wrapped value is unchanged. """
def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap('lego')
    with pytest.raises(Exception) as e:
        present.wrap('candle')
    assert present.unwrap() == 'lego'