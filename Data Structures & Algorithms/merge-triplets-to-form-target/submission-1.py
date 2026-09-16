class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flags = [0,0,0]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                triplets[i] = [0,0,0]
                continue
            
            if triplets[i][0] == target[0]:
                flags[0] = 1
            if triplets[i][1] == target[1]:
                flags[1] = 1
            if triplets[i][2] == target[2]:
                flags[2] = 1
        
        return flags == [1,1,1]
            

        


