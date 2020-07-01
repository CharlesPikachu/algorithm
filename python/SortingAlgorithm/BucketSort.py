'''
Function:
    桶排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''桶排序(假设都是整数)'''
def BucketSort(array):
    max_value, min_value, length = max(array), min(array), len(array)
    buckets = [0 for _ in range(min_value, max_value+1)]
    for i in range(length):
        buckets[array[i]-min_value] += 1
    output = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            output += [i+min_value] * buckets[i]
    return output


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = BucketSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))