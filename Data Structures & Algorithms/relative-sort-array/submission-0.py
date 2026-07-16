class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ind = {}
        count = {}
        for i in range(len(arr2)):
            if arr2[i] not in ind:
                ind[arr2[i]] = i
        end = []
        for i in range(len(arr1)):
            if arr1[i] not in ind:
                end.append(arr1[i])
            if arr1[i] in ind:
                if arr1[i] not in count:
                    count[arr1[i]] = 0
                count[arr1[i]]+=1
        end.sort()
        ret = sorted(ind.items(), key=lambda x:x[1])
        print(ret)
        print(count)

        ans = []
        for key in ret:
            num = key[0]
            for _ in range(count[num]):
                ans.append(num)
        ans = ans + end
        return ans
