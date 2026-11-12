from ft_filter import ft_filter
import sys


def filterstring():
    arg = sys.argv[1:]
    try:
        if len(arg) != 2:
            raise AssertionError(
                "AssertionError: the arguments are bad")
        try:
            length = int(arg[1])
        except ValueError:
            raise AssertionError("AssertionError: the arguments are bad")
        words = [w for w in arg[0].split(" ") if w]
        print(ft_filter(lambda word: len(word) > length, words))
    except AssertionError as a:
        print(a)


if __name__ == "__main__":
    filterstring()
