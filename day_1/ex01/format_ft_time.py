import time as t


def main():
    """
    printing time in spescific format.
    """

    print(
        "Seconds since January 1, 1970:",
        t.time(),
        "or",
        t.time().__format__(".2e"),
        "in scientific notation"
    )
    print(t.strftime("%b %d %Y", t.localtime()))


if __name__ == "__main__":
    main()
