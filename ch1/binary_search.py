# !/bin/env python3


def search(l, el):
    """A function that applies binary search on a sorted indexed object.
    Args:
        l: sorted indexed object
        el: element
    Complexity:
        O(log(n))
    """

    s = 0
    e = len(l) - 1
    m = (e + s) // 2
    while (s < e):
        if el > l[m]:
            s = m + 1
        elif el < l[m]:
            e = m - 1
        else:
            return m

        m = (e + s // 2)

    return None


if __name__ == "__main__":

    r = range(0, 5500)

    i = search(r, 557)
    if i is not None:
        print("Element found at {:d}"
              .format(i))

    print(search.__doc__)
