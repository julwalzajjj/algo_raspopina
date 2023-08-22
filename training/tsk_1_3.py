# Given a string s, reverse the order of characters in 
# each word within a sentence while still preserving whitespace 
# and initial word order.



s = input()

def reverse_str(s):
    # s_list = s.split()
    # reversed_list = []
    # for i in s_list:
    #     reversed_list.append(i[::-1])
    # return ' '.join(reversed_list)

    reversed_list = ' '.join(map(lambda x : x[::-1], s.split()))
    return reversed_list

print(reverse_str(s))