import os


def terminal_columns() -> int:
    """ return terminal columns """
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def ft_tqdm(lst: range) -> None:
    """ draw progress bar like tqdm """
    t_columns = terminal_columns()
    total = len(lst)
    count = 0
    for element in lst:
        yield element
        count += 1
        percent = (count * 100) // total
        left = f"{percent:3}%|["
        right = f"|] {count}/{total}"
        bar = max(1, t_columns - len(left) - len(right))
        progress = ("=" * ((count * bar // total) - 1) + ">").ljust(bar)
        print(f"\r{left}{progress}{right}", end="", flush=True)
