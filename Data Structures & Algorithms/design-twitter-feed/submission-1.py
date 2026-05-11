class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.insert(0, [userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        if userId in self.follows:
            userFollows = self.follows[userId]
        else:
            userFollows = {}
        for i in range(len(self.tweets)):
            curId, tweetId = self.tweets[i]
            if  curId == userId or curId in userFollows:
                ret.append(tweetId)
            if len(ret) == 10:
                break
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
