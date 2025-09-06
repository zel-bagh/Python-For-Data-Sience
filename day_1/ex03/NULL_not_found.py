def NULL_not_found(object: any) -> int:
    """
    A function that prints the object type of all types of "Null".
    Return 0 if it goes well and 1 in case of error.
    """

    if (object is None):
        print("Nothing: None", type(object))
    elif (object == 0 and type(object) is int):
        print("Zero: 0", type(object))
    elif (object is False):
        print("Fake: False", type(object))
    elif (object == ""):
        print("Empty:", type(object))
    elif (object != object):
        print("Cheese: nan", type(object))
    else:
        print("Type not found")
        return 1
    return 0
