# Вам дана строка s, состоящая из символов 'a', 'b' и 'c', и неотрицательное целое число k. Каждую минуту вы можете взять 
# либо самый левый символ 
# из s, либо самый правый символ из s.

# Верните минимальное количество минут, необходимое для того, чтобы взять как минимум 
# k каждого символа, или верните -1, если невозможно взять k каждого символа.

def search(s, k):
    s_list = list(s)

    l = 0
    r = len(s_list) - 1

    minutes = 0
    d = {'a' : 0, 
         'b' : 0, 
         'c' : 0}
    
    while l < r:
        d[s_list[l]] += 1
        minutes += 1
        if d['a'] >= k and d['b'] >= k and d['c'] >= k:
            return minutes
        
        d[s_list[r]] += 1
        minutes += 1
        if d['a'] >= k and d['b'] >= k and d['c'] >= k:
            return minutes
        
        s_list.pop(r)
        s_list.pop(l)

        r = len(s_list) - 1

    return -1


s = input()
k = int(input())

print(search(s, k))
