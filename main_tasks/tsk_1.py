a = [int(x) for x in input().split()]

def bubble(a):
    for i in range(1, len(a)):
        for j in range(len(a) - i):
            if a[j] > a[j + 1]:
                tmp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = tmp
    return a

print(bubble(a))



    
