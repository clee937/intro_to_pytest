from lib.string_builder import *

""" Testing StringBuilder output is an empty string on initialisation"""
def test_string_builder_output_on_initialisation():
    sb = StringBuilder()
    result = sb.output()
    assert result == "", "Should return empty string"

""" Testing StringBuilder output with 'Hello World!'"""
def test_string_builder_output_on_single_string():
    sb = StringBuilder()
    sb.add("Hello, World!")
    result = sb.output()
    assert result == "Hello, World!", "Should return \'Hello, World\'"

""" When we add multiple strings, the ouput is those strings concatenated"""
def test_string_builder_output_on_multiple_strings():
    sb = StringBuilder()
    sb.add("Hello ")
    sb.add("World")
    result = sb.output()
    assert result == "Hello World", "Should return \'Hello World\'"
    
""" Testing StringBuilder size with 'Hello World'"""
def test_string_builder_size():
    sb = StringBuilder()
    sb.add("Hello, World!")
    result = sb.size()
    assert result == 13, "Should return 13"

""" Testing StringBuilder size for multiple strings. Should return the length of all the strings concatenated."""
def test_string_builder_size_on_multiple_strings():
    sb = StringBuilder()
    sb.add("Hello ")
    sb.add("World")
    result = sb.size()
    assert result == 11, "Should return 11"