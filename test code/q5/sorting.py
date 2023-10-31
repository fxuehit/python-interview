import random

#O(N*logN)
def quick_sort(float_list):
    if len(float_list) <= 1:
        return float_list
    else:
        # 随机选择一个元素作为基准元素
        pivot = random.choice(float_list)
        left = [x for x in float_list if x < pivot]
        right = [x for x in float_list if x > pivot]
        equal = [x for x in float_list if x == pivot]
        return quick_sort(left) + equal + quick_sort(right)

arr = [12.28, 11.30, 13.55, 5.10, 6.70, 7.81]
sorted_fl = quick_sort(arr)
print("随机快速排序后的数组：", sorted_fl)

# question: is this superior than bubble sorting and why?