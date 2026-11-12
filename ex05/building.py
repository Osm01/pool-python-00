import sys
import string


def count(arg: str) -> dict:
    return {
        "upper letters": sum(1 for c in arg if c.isupper()),
        "lower letters": sum(1 for c in arg if c.islower()),
        "punctuation marks": sum(1 for c in arg if c in string.punctuation),
        "spaces": sum(1 for c in arg if c.isspace()),
        "digits": sum(1 for c in arg if c.isdigit()),
    }


def main():
    args = sys.argv[1:]
    try:
        if len(args) > 1:
            raise AssertionError(
                "more than one argument is provided to the program")
    except AssertionError as a:
        return print(a)

    if args and args[0]:
        txt = args[0]
    else:
        print("What is the text to count?")
        txt = sys.stdin.readline()
    print(f"The text contains {len(txt)} characters:")
    for key, value in count(txt).items():
        print(f"{value} {key}")


if __name__ == "__main__":
    main()
