import numpy as np

a = [int(x) for x in input().split()]

def choose_sort(a):
    for i in range(len(a) - 1):
        local_min = np.max(a) + 1
        for j in range(i, len(a)):
            if a[j] < local_min:
                local_min = a[j]
                local_min_idx = j

        tmp = a[local_min_idx]
        a[local_min_idx] = a[i]
        a[i] = tmp 
    
    return a

print(choose_sort(a))

        



            