class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        #print("new user being created")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
#user_1.id = "001"
#user_1.username = "angela"

print(user_1.username)

user_2 = User("002","jack")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)