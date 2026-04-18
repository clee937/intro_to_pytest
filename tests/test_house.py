from lib.house import *

""" When we build a new house, it needs to be given a house number and starting door colour. Those and the starting door colour are stored in attributes """
def test_that_correct_attributes_are_stored_after_instantiation():
    house = House(137, "white")
    assert house.house_number == 137, "house number should be 137"
    assert house.door_colour == "white", "door colour should be white"
    assert house.number_of_floors == 2, "number of floors should be 2"

""" When we have a house, the key details can be got back """
def test_that_details_can_be_retrieved():
    house = House(137, "white")
    assert house.get_details() == "House number 137 has 2 floors and a white door.", "Should return 'House number 137 has 2 floors and a white door.'"

""" When we have a house, and we change its door colour, this is reflected in its attribute """
def test_repaint_door():
    house = House(137, "white")
    house.repaint_door("green")
    assert house.door_colour == "green", "door colour should be 'green'"
