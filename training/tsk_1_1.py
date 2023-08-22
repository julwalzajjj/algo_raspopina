
# Вам дан целочисленный массив nums с индексацией с 0 и целевой элемент target.

# Целевым индексом является индекс i такой, что nums[i] == target.

# Верните список целевых индексов для nums после сортировки nums в порядке неубывания. 
# Если целевых индексов нет, верните пустой список. Возвращаемый список должен быть 
# отсортирован в порядке возрастания.

a = [int(x) for x in input().split()]
number = int(input())
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr

def index_search(nums, target):
    # sorting 
    sorted_nums = merge_sort(nums)
    indexes = []
    for i in range(len(nums)):
        if sorted_nums[i] == target:
            indexes.append(i)
    
    return indexes

print(index_search(a, number))