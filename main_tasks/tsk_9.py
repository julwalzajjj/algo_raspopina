# правильная скобочная последовательность

import collections

s = input()

def PCB(s):
    s_list = list(s)

    q = collections.deque()
    skob = {'(':')', '[':']', '{':'}'}

    for i in s_list:
        if i in skob.keys():
            q.append(i)
        else:
            if skob[q.pop()] != i:
                return False

    if len(q) == 0:
        return True
    else:
        return False




