def ft_filter(function, iterator) -> list:
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""
    if function is None:
        return [item for item in iterator if item]
    return [item for item in iterator if function(item)]
