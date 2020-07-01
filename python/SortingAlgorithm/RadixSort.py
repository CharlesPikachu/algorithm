'''
Function:
    基数排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''基数排序(假设都是整数)'''
def RadixSort(array):
    max_value = max(array)
    num_digits = len(str(max_value))
    for i in range(num_digits):
        buckets = [[] for k in range(10)]
        for j in array:
            buckets[int(j / (10 ** i)) % 10].append(j)
        output = [m for bucket in buckets for m in bucket]
    return output


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = RadixSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))