from lib.gratitudes import *

""" Tests that gratitude list is empty on initialisation"""
def test_gratitude_list_is_empty_on_initialisation():
    gratitudes = Gratitudes()
    assert gratitudes.gratitudes == []

""" When we add a gratitude, it should be added to the gratitude list"""
def test_gratitude_is_added_to_gratitudes_list_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("coffee")
    assert gratitudes.gratitudes == ["coffee"]

""" When we add multiple gratitudes, they should be added to the gratitude list"""
def test_multiple_gratitudes_are_added_to_gratitudes_list_correctly():
    gratitudes = Gratitudes()
    gratitudes.add("the sun")
    gratitudes.add("coffee")
    gratitudes.add("tea")
    assert gratitudes.gratitudes == ["the sun", "coffee", "tea"]
    

""" When we format a gratitude, it should return the formatted version"""
def test_formatted_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("the sun")
    result = gratitudes.format()
    assert result == "Be grateful for: the sun"

""" When we format a gratitude, it should return the formatted version for multiple gratitudes"""
def test_multiple_formatted_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("the sun")
    gratitudes.add("tea")
    gratitudes.add("cake")
    result = gratitudes.format()
    assert result == "Be grateful for: the sun, tea, cake"
