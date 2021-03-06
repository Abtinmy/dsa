"""
    *** Time Complexity ***
    * Best case : O(N)
    * Worst case : O(N^2)
    * Average : O(NlogN^2) or O(N^(3/2)) -> dependes on gap length
    
    * Space complexity = O(1)
    * In-Place sort
    * Not Stable sort
"""


from sorts.insertion import insertionsort


def shellsort(arr):
    res = arr.copy()
    gap = len(res) // 2
    
    while gap > 0:
        left = 0
        right = gap

        while right < len(res):
            if res[left] > res[right]:
                res[left], res[right] = res[right], res[left]
            right += 1
            left += 1
            
        gap //= 2
    
    return insertionsort(res)

