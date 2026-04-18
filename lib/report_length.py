def report_length(string):
    if type(string) == str:
    # if isinstance(string, str):
        length = len(string)
        return f"This string was {length} characters long."
    else:
        return "Not a string"
    