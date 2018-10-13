# !/bin/env python
# -*- coding: utf-8 -*-


def length(li):
    if li == []:
        return 0
    elif li[0] == [li[0]]:
        return 1
    else:
        return 1 + length(li[1:])


if __name__ == "__main__":
    print(length([1, 2, 3]*100))
