# !/bin/env python
# -*- coding: utf-8 -*-


def min(arr, s, e):
    """find minimum in array
    Arguments:
        arr: array
    """

    min = arr[s]
    index = s
    for i in range(s+1, e+1):
        if arr[i] < min:
            min = arr[i]
            index = i

    return index


def selection_sort(arr):
    """selection sort on an arrayi
    Arguments:
        arr: array
    """

    i = 0
    while i < len(arr):
        j = min(arr, i, len(arr)-1)
        arr[i], arr[j] = arr[j], arr[i]
        i += 1


if __name__ == "__main__":
    arr = [2, -1, 3]
    selection_sort(arr)
    print(arr)
