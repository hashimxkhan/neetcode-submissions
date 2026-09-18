class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i >= 0:
            total = digits[i] + carry
            if total < 10:
                carry = 0
            total = total % 10
            digits[i] = total
            if not carry:
                break
            i-=1
        if carry:
            digits.insert(0,1)
        return digits
