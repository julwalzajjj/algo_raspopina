# 2 указателя
a = [int(x) for x in input().split()]
n, t = int(input()), int(input())

def books(books_list, n, t):
    s = 0
    res = 0
    for r in range(n):
        s += books_list[r]
        l = 0
        while s > t:
            l += 1
            s -= books_list[l]
        res = max(res, r - l + 1)

    return res

print(books(a, n, t))