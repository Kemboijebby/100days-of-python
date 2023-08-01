
import random
data=[
    {'name':'Christiano Ronaldo',
     'follower_count':246,
     'description':'footballer',
     'country':'portugal'},

    {'name':'Nicki minaj',
     'follower_count':301,
     'description':'Musician & Rapper',
     'country':'New york',
     },
     {'name':'Justin Beiber',
      'follower_count':220,
      'description':'musician',
      'country':'Mexico',
     },
    {'name':'Rihanna',
     'follower_count':299,
     'description':'musician,Business-lady',
     'country':'Barbados',
     },
    {'name':'Travis scott',
     'follower_count':150,
     'description':'Rapper',
     'country':'USA',
     },
    {'name':'Kylie Jenner',
     'follower_count':225,
     'description':'Business lady,Actress',
     'country':'USA',
     },
    {'name':'Kim Kardashian',
     'follower_count':297,
     'description':'Actress,Business-woman and a lawyer',
     'country':'USA',
     },
    {'name':'Khloe Kardashian',
     'follower_count':190,
     'description':'Actress and Business-woman',
     'country':'USA',
     },
    {'name':'Arian Grande',
     'follower_count':187,
     'description':'Musician',
     'country':'USA',
     } ,
    {'name':'Camilla Cabello',
     'follower_count':155,
     'description':'Musician',
     'country':'Mexico'},

    {'name':'Anitah kemboi',
     'follower_count':500,
     'description':'Programmer and Business-lady',
     'country':'Kenya',
     }
]
def get_random_account():
    """ Get data from a random account"""
    return random.choice(data)

def format_data(account):
    """format  data into a printable format:name,description and country"""
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return (f"{name},a {description},from {country}")

def check_answer(guess,a_followers,b_followers):
    """checks followers against user's guess and returns True of they got
    it right.Or false if they got it wrong"""
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"

def game():
    score=0
    game_should_continue=True
    account_a=get_random_account()
    account_b=get_random_account()
    while game_should_continue:
        account_a=account_b
        account_b=get_random_account()

        while account_a == account_b:
             account_b = get_random_account()
        print(f"compare A:{format_data(account_a)}.")
        print("vs")
        print(f"against B:{format_data(account_b)}.")

        guess=input("Who has more followers?Type'A' or 'B':").lower()
        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        is_correct=check_answer(guess,a_follower_count,b_follower_count)

        if is_correct:
            score+=5
            print(f"You're right! current score is {score}")
        else:
            game_should_continue=False
            print(f"sorry,that's wrong.Final score is {score}")

game()





































