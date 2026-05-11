class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        ans = 0
        r = len(people) - 1
        while l <= r:
            left = limit - people[r]
            ans+=1
            r-=1
            if left >= people[l]:
                l+=1

        return ans




