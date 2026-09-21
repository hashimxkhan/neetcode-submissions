class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hands = {}
        heap = hand.copy()
        heapq.heapify(heap)
        for card in hand:
            if card not in hands:
                hands[card] = 0
            hands[card]+=1
        
        groups = len(hand) / groupSize
        cur = 0
        while heap:
            val = heapq.heappop(heap)
            if hands[val] == 0:
                continue
            hands[val]-=1
            for i in range(groupSize - 1):
                if val+1 not in hands or hands[val+1] == 0:
                    return False
                hands[val+1]-=1
                val+=1
            cur+=1
        return cur == groups
            
