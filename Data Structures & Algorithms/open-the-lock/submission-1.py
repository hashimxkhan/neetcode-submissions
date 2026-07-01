class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for deadend in deadends:
            visited.add(deadend)
        
        q = deque()
        q.append(("0000", 0))

        while q:
            combo, turns = q.popleft()
            if combo in visited:
                continue
            if combo == target:
                return turns
            visited.add(combo)
            for i in range(4):
                d = int(combo[i])
                for diff in (-1, +1):
                    new = (d + diff) % 10
                    child = combo[:i] + str(new) + combo[i+1:]
                    q.append((child, turns+1))
        return -1

