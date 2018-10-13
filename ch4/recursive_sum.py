# !/bin/env python
# -*- coding: utf-8 -*-


def sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


if __name__ == "__main__":
    print(sum(range(0, 10**5)))
