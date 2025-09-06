def all_thing_is_obj(object: any) -> int:
    """
    Prints the type of the given object and always returns 42.
    """

    if (type(object).__name__ in ("tuple", "list", "set", "dict")):
        print(type(object).__name__.capitalize(), ":", type(object))
    elif (type(object).__name__ == "str"):
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42
