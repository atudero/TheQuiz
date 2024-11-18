class User:
    def __init__(self, user_id, username):
        print("Creating a new user...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def increase_followers(self):
        self.followers+=1

    def follow(self, user):
        self.following+=1
        user.followers+=1




user_1 = User("001", "Angel")
#user_1.id = "001"
#user_1.username = "Angel"

print(user_1.username)

user_2 = User("002", "Peter")
#user_2.id = "002"
#user_2.username = "Peter"

print(user_2.id)

user_2.follow(user_1)

print(user_2.followers)
print(user_1.followers)