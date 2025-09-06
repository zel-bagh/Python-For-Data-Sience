import sys


def count_characters(text: str) -> dict:
    """
    This function counts the number of each character type in a given text.
    """
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    characters = {"upper letters": 0, "lower letters": 0,
                  "digits": 0, "spaces": 0, "punctuation marks": 0}
    for char in text:
        if char.isupper():
            characters["upper letters"] += 1
        elif char.islower():
            characters["lower letters"] += 1
        elif char.isdigit():
            characters["digits"] += 1
        elif char.isspace():
            characters["spaces"] += 1
        elif char in punctuation_marks:
            characters["punctuation marks"] += 1
    return characters


def main():
    """
    Print an error message if more than one argument is provided.
    Prompt the user for a text if no argument is provided.
    Count the number of each character type in the given text.
    """


text = ""

try:
    if (sys.argv.__len__() > 2):
        raise AssertionError("AssertionError: " +
                             "more than one argument is provided")
    elif (sys.argv.__len__() == 2):
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        text = sys.stdin.readline()

    print("The text contains", text.__len__(), "characters:")
    characters = count_characters(text)
    for key, value in characters.items():
        print(value, key)

except AssertionError as e:
    print(e)
except KeyboardInterrupt:
    print("\nGoodbye!")

if __name__ == "__main__":
    main()
