class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username},it's {self.username}")


user1 = User("Dark", "Dark@gmail.com" , "444")
user2 = User("Bat", "Bat@outlook.com", "ddd")

user1.email = "New@gmail.com"
print("user email:", user1.email)

user1.say_hi_to_user(user2)
