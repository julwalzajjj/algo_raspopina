a = [int(x) for x in input().split()]

def insert_sort(a_in):
    a = a_in.copy()
    for i in range(1, len(a)):
        insert_idx = len(a) + 1
        insert_el = a[i]
        for j in range(len(a[:i])):
            if a[i] < a[:i][j]:
                insert_idx = j
                break
        if insert_idx == len(a) + 1:
            insert_idx = i
        else:
            a.pop(i)
            a = a[:insert_idx] + [insert_el] + a[(insert_idx):]  
    return a

print(insert_sort(a))



            
        