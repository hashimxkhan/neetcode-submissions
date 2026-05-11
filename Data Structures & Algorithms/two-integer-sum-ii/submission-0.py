class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers) - 1
        while l < h:
            cur = numbers[l] + numbers[h]
            if cur == target:
                return [l+1, h+1]   
            elif cur > target:
                h-=1
            else:
                l+=1    