import sys
from ft_filter import ft_filter


def main():
    """
    Accepts only 2 arguments:
    1. string
    2. integer

    Returns a list of words that are longer than the integer.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Exactly two arguments \
                (string and integer) are required.")

        text = sys.argv[1]
        n = int(sys.argv[2])

        filtered_words = ft_filter(lambda word: len(word) > n, text.split())

        print(filtered_words)

    except ValueError:
        print("AssertionError:", "second argument must be an integer.")
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
