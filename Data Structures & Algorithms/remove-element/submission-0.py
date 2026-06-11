class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        k = 0
        for num in nums:
            if num != val:
                temp.append(num)
                k+=1
        nums[:] = temp
        return k
            
