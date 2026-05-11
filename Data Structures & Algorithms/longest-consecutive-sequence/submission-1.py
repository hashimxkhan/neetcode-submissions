class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        cur = 0
        my_set = set()
        for num in nums:
            my_set.add(num)
        for num in nums:
            if num-1 not in my_set:
                cur=1
                curNum = num
                while curNum+1 in my_set:
                    cur+=1
                    curNum+=1
            if cur > longest:
                longest = cur
        return(longest)


        

        