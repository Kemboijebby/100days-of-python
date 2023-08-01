import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

user_cards=[]
computer_cards=[]
is_game_over=False

def calculate_scores(cards):

    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose,opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, you lose"
    elif user_score > computer_score:
        return 'you win'
    else:
        return "You lose"

while not is_game_over:
    user_score=calculate_scores(user_cards)
    computer_score=calculate_scores(computer_cards)
    print(f"Your cards:{user_cards},current score:{user_score}")
    print(f"computer first card:{computer_cards [0]}")
    if user_score==0 or computer_score==0 and user_score>21:
        is_game_over=True
    else:
        second_deal= input("Do you want to draw another card? type y yes and n for pass ")
        if second_deal=="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True
while computer_score!=0 and computer_score<16:
    computer_cards.append(deal_card())
    computer_score=calculate_scores(computer_cards)
print(f"Your final hand:{user_cards},final score{user_score}")
print(f"computers final hand:{computer_cards},final score:{computer_score}")
print(compare(user_score,computer_score))




