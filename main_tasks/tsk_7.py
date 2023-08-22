# 2 указателя
a = [int(x) for x in input().split()]

def max_sum(a):
    s1 = 0
    s2 = 0
    res = 0
    r = len(a) - 1
    for l in range(len(a)):
        s1 = sum(a[:l])
        while s2 < s1:
            s2 = sum(a[r:])
            r -= 1
        if s1 == s2 and r > l:
            res = max(res, s1)
    return res

print(max_sum(a))

    

    
