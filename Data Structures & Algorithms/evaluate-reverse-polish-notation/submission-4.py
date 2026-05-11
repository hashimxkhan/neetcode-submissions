class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = [ "+", "-", "*", "/"]
        for char in tokens:
            if char in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                match char:
                    case "+":
                        ans = num1 + num2
                    case "-":
                        ans = num1 - num2
                    case "*":
                        ans = num1 * num2
                    case "/":
                        if num2 == 0:
                            ans = 0
                        else:
                            ans = num1 / num2
                stack.append(int(ans))
            else:
                stack.append(int(char))
        return stack.pop()

        