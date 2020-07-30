'''
Function:
    最小的k个数
Author:
    Charles
'''
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def QuickSort(arr, left, right):
            if left >= right: return
            i, j, partition = left, right, arr[left]
            while i < j:
                while i < j and arr[j] >= partition: j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] <= partition: i += 1
                arr[j] = arr[i]
            arr[i] = partition
            QuickSort(arr, left, i-1)
            QuickSort(arr, i+1, right)
        QuickSort(arr, 0, len(arr)-1)
        return arr[:k]