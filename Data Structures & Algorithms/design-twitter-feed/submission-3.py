class Twitter:

    def __init__(self):
        self.users_tweets = {}
        self.num_tweets = 0
        self.users_following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users_tweets:
            self.users_tweets[userId] = []
        self.users_tweets[userId].append([tweetId, self.num_tweets])
        self.num_tweets+=1        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        tweets = []
        if userId not in self.users_following:
            return []
        for user in self.users_following[userId]:
            if user in self.users_tweets:
                for tweet in self.users_tweets[user]:
                    tweets.append(tweet)
        tweets.sort(key=lambda x : -x[1])
        ret = []
        for i in range(10):
            if i >= len(tweets):
                break
            ret.append(tweets[i][0])
        return ret

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users_following:
            self.users_following[followerId] = set()
        self.users_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_following[followerId]:
            self.users_following[followerId].remove(followeeId)        
