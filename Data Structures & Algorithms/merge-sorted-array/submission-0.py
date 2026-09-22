class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        j = len(nums1) - len(nums2)
        for num in nums2:
            nums1[j] = num
            j+=1
        nums1.sort()
        