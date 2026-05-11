class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "+":
                    num3 = num1 + num2
                elif token == "-":
                    num3 = num2 - num1
                elif token == "*":
                    num3 = num1 * num2
                else:
                    num3 = int(num2 / num1)
                stack.append(num3)
        return stack.pop()
