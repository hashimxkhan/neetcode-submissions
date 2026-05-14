class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            elif not (stack[-1] > 0 and ast < 0):
                stack.append(ast)
                continue
            while stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                if abs(stack[-1]) > abs(ast):
                    break
                else:
                    stack.pop()
                    if not stack or not (stack[-1] > 0 and ast < 0):
                        stack.append(ast)
        return stack

