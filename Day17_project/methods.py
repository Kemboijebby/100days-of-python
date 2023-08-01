# creating methods
# when functions are attached to objects they are called methods
# class Car:
#     def enter_race_mode(self):
#         self.seats = 2
class User:

    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers += 1
        self.following += 1
user_1=User("001","Anitah")
user_2=User("001","kemboi")
print(user_2.followers)
print(user_2.following)
