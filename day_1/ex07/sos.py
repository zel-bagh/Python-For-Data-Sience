import sys


def main():
    """
    Encode a string into Morse code. Letters/digits → . and -, spaces → /
    """

    NESTED_MORSE = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
        " ": "/"
    }
    try:
        if len(sys.argv) != 2:
            raise AssertionError("One argument is required")

        text = sys.argv[1].upper()

        morse_code = ""
        for char in text:
            if char not in NESTED_MORSE:
                raise AssertionError("The argument is bad")
            morse_code += NESTED_MORSE[char] + " "

        morse_code = morse_code.strip()
        print(morse_code)

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
