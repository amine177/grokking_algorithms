# !/bin/env python
# -*- coding: utf-8 -*-


def search(li, e):
    if len(li) == 0:
        return False
    elif len(li) == 1:
        return li[0] == e

    else:
        m = (len(li) - 1) // 2
        if li[m] > e:
            return search(li[:m-1], e)
        elif li[m] < e:
            return search(li[m+1:], e)
        else:
            return True


if __name__ == "__main__":
    print(search([1, 2, 3], 4))
