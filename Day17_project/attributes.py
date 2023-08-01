#attributes are components of an object

class User:

    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.follower=250

user_1=User("001","Anitah")
user_2=User("001","kemboi")
print(user_1.id)
print(user_2.follower)
