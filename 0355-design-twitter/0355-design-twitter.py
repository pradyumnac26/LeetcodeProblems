class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list) 
        self.followerList = defaultdict(set)
        self.time = 0 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1 
        self.tweets[userId].append((self.time, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        res = [] 
        following = set(self.followerList[userId] )
        following.add(userId) 
        for f in following : 
            feed = feed + self.tweets[f]
        feed.sort(key=lambda x:x[0] , reverse = True) 
        for t, teets in feed : 
            res.append(teets)
        return res[:10]


        


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerList[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerList[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)