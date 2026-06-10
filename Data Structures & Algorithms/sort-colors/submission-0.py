class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        mapp = {0: 0, 1 : 0, 2 : 0}
        for num in nums:
           mapp[num]+=1
        print(mapp)
        
        count = 0
        for key in [0,1,2]:
            print(key)
            for i in range(count, count + mapp[key]):
                nums[i] = key
            count+= mapp[key]


            


        