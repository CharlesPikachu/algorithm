'''
Function:
    希尔排序
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import random


'''希尔排序'''
def ShellSort(array):
    length = len(array)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j, cur = i, array[i]
            while (j - gap >= 0) and (cur < array[j - gap]):
                array[j] = array[j - gap]
                j = j - gap
            array[j] = cur
        gap = gap // 2
    return array


'''test'''
if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    array_sort = ShellSort(array.copy())
    print('INPUT:\n%s' % ','.join([str(i) for i in array]))
    print('OUTPUT:\n%s' % ','.join([str(i) for i in array_sort]))