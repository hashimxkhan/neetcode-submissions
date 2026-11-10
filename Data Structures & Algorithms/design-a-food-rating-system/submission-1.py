class Food:
    def __init__(self, food, cuisine, rating):
        self.food = food
        self.cuisine = cuisine
        self.rating = rating

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        for i in range(len(foods)):
            food = Food(foods[i], cuisines[i], ratings[i])
            self.foods[foods[i]] = food
    def changeRating(self, food: str, newRating: int) -> None:
        self.foods[food].rating = newRating
    def highestRated(self, cuisine: str) -> str:
        food = []
        highestRated = []
        for f in self.foods:
            cur = self.foods[f]
            if cur.cuisine == cuisine:
                if not highestRated:
                    highestRated = [f, cur.rating]
                elif highestRated[1] == cur.rating:
                    if f < highestRated[0]:
                        highestRated = [f, cur.rating]
                elif highestRated[1] < cur.rating:
                    highestRated = [f,cur.rating]
        return highestRated[0]
