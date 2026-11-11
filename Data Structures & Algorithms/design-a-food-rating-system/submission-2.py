class Food:
    def __init__(self, food, cuisine, rating):
        self.food = food
        self.cuisine = cuisine
        self.rating = rating

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.heaps = {}
        for i in range(len(foods)):
            food = Food(foods[i], cuisines[i], ratings[i])
            self.foods[foods[i]] = food
            if cuisines[i] not in self.heaps:
                self.heaps[cuisines[i]] = []
            self.heaps[cuisines[i]].append([-ratings[i], foods[i]])
        for cuisine in self.heaps:
            heapq.heapify(self.heaps[cuisine])
    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food].rating = newRating
        cuisine = self.foods[food].cuisine
        heapq.heappush(self.heaps[cuisine], [-newRating, food])
    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        while heap:
            cur = heapq.heappop(heap)
            if self.foods[cur[1]].rating == (cur[0] * -1):
                return cur[1]
            
