# !/bin/env python3
# -*- coding: utf-8 -*-


def quicksort(arr, s, e):
    if s <= e:
        pivot = arr[s]
        pivoti = s
        for i in range(s+1, e+1):
            if arr[i] <= pivot:
                tmp = arr[i]
                j = i
                while j > pivoti:
                    arr[j] = arr[j-1]
                    j -= 1
                arr[pivoti] = tmp
                arr[pivoti+1] = pivot
                pivoti += 1
        quicksort(arr, s, pivoti-1)
        quicksort(arr, pivoti+1, e)


if __name__ == "__main__":
    x = [0, -1, -5, 3, 5, 23, -2]
    quicksort(x, 0, len(x)-1)
    print(x)
