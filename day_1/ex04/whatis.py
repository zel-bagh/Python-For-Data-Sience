import sys


def check_odd_or_even(number: int) -> str:
    """
    This function checks if the given integer is odd or even.
    """
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


def main():
    """
    Check if the given argument is an integer and print if it's odd or even.
    Print an error message if the argument is not an integer or
    if more than one argument is provided.
    """
    try:
        if (sys.argv.__len__() > 2):
            raise AssertionError("more than one argument is provided")
        elif (sys.argv.__len__() != 1):
            print(check_odd_or_even(int(sys.argv[1])))

    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
