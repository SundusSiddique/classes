# classes
## python classes
class InstagramAccount:
    def __init__(self, username, followers, following, ID, age):
        self.username = username
        self.followers = followers
        self.following = following
        self.ID = ID
        self.age = age

    def display(self):
         return "Username: " + self.username + ", Followers: " + str(self.followers) + ", Following: " + str(self.following) + ", ID: " + self.ID + ", Age: " + str(self.age)
    def famous(self):
        if self.followers >= 10000:
            return "@" + self.username + " is famous!"
        else:
            return "@" + self.username + " is not famous yet."

instagram_account1 = InstagramAccount("johndoe", 12000, 800, "johndoe123", 25)
instagram_account2 = InstagramAccount("janedoe", 9000, 900, "janedoe123", 30)
instagram_account3 = InstagramAccount("alice", 15000, 1000, "alice123", 35)

print(instagram_account1.display()) # Output: "Username: johndoe, Followers: 12000, Following: 800, ID: johndoe123, Age: 25"
print(instagram_account1.famous()) # Output: "@johndoe is famous!"
print(instagram_account2.display()) # Output: "Username: janedoe, Followers: 9000, Following: 900, ID: janedoe123, Age: 30"
print(instagram_account2.famous()) # Output: "@janedoe is not famous yet."
print(instagram_account3.display()) # Output: "Username: alice, Followers: 15000, Following: 1000, ID: alice123, Age: 35"
print(instagram_account3.famous()) # Output: "@alice is famous!"
