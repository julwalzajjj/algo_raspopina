# 2 указателя
a = [int(x) for x in input().split()]

def diff(puples_list):
    res = 0
    sorted_list = sorted(puples_list)
    for r in range(len(puples_list)):
        l = 0

        while sorted_list[r] - sorted_list[l] > 5:
            l += 1
            
        res = max(res, r - l + 1)

    return res

print(diff(a))