
# creating a class
class User:
    def __init__(self, user_id, username, follower):
        self.user_id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    # creating method inside a class
    def follow(self, user):
        user.follower += 1
        self.following += 1


# creating objects from User class
user_1 = User("001", "Richard")
user_2 = User("002", "Michael")

