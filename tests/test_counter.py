from lib.counter import *

"""Testing that the count is 0 on initialisation"""
def test_that_counter_is_zero_on_initialisation():
    my_counter = Counter()
    assert my_counter.report() ==  "Counted to 0 so far.", "Should return 0"


def test_reports_the_correct_count_when_adding_once():
    my_counter = Counter()
    my_counter.add(5)
    result = my_counter.report() 
    assert result == "Counted to 5 so far.", "Testing with adding 5 once. Should return 5"

def test_reports_the_correct_count_when_adding_twice():
    my_counter = Counter()
    my_counter.add(5)
    my_counter.add(3)
    result = my_counter.report() 
    assert result == "Counted to 8 so far.", "Testing with adding 5 and then 3. Should return 8"