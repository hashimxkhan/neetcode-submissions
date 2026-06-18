class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for person in details:
            age = person[11] + person[12]
            age = int(age)
            if age > 60:
                count+=1
        return count