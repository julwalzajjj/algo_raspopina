# Вам дан целочисленный массив nums с индексацией с 0, значения 
# которого строго возрастают, и положительное целое число diff. Тройка (i, j, k) 
# является арифметической тройкой, если выполнены следующие условия:

# i < j < k,
# nums[j] - nums[i] == diff, и
# nums[k] - nums[j] == diff.
# Верните количество уникальных арифметических троек.

a = [int(x) for x in input().split()]
diff = int(input())

def count_3(nums, diff):
    n = len(nums)
    i = count = 0
    j = 1
    k = 2

    while i < n and j < n and k < n:
        if nums[j] - nums[i] > diff:
            i += 1
        elif nums[j] - nums[i] < diff:
            j += 1
        else:
            if nums[k] - nums[j] > diff:
                j += 1
            elif nums[k]- nums[j] < diff:
                k += 1
            else:
                count += 1
                k += 1

    return count

print(count_3(a, diff))