import sys


def parse_data(inp: str) -> int:
    try:
        return int(inp)
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")


def handle_input():
    args = sys.argv[1:]
    if len(args) == 0:
        return
    try:
        if len(args) > 1:
            raise AssertionError(
                "AssertionError: more than one argument is provided")
        num = parse_data(args[0])
    except AssertionError as a:
        return print(a)
    print("I'm Even." if num % 2 == 0 else "I'm Odd.")


if __name__ == "__main__":
    handle_input()
