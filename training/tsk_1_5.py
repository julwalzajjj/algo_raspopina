# Дана строка licensePlate и массив строк words, найдите самое короткое завершающее слово в words.

# Завершающим словом является слово, которое содержит все буквы из licensePlate. 
# Игнорируйте числа и пробелы в licensePlate и рассматривайте буквы как нечувствительные к регистру. 
# Если буква появляется в licensePlate более одного раза, то она должна появляться в слове такое же количество 
# раз или более.

# Например, если licensePlate = "aBc 12c", то он содержит буквы 'a', 'b' (не учитывая регистр) и 'c' 
# дважды. Возможные завершающие слова - это "abccdef", "caaacab" и "cbca".

# Верните самое короткое завершающее слово из words. Гарантируется, что ответ существует. Если есть несколько
# самых коротких завершающих слов, верните первое из них, которое встречается в words.

import numpy as np


def licence(lic):
    d = {}
    lic_lower = lic.lower()
    lic_list = list(lic_lower)
    for letter in lic_list:
        if letter.isalpha():
            d[letter] = d.get(letter, 0) + 1
    return d


def licensePlate(lic, l_words):
    len_word = np.inf
    d = licence(lic)
    for word in l_words:
        d_itt = d.copy()
        for letter in word:
            if d_itt.get(letter, -1) != -1:
                d_itt[letter] -= 1
            if sum(d_itt.values()) == 0:
                break
        
        if sum(d_itt.values()) == 0:
            if len_word > len(word):
                len_word = len(word)
                stop_word = word
    return stop_word

lic = input()
list_words = [x for x in input().split()]

print(licensePlate(lic, list_words))



