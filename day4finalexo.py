a="rock"
b="paper"
c="scissors"
game_images= ["rock", "paper", "scissors"]
import random
user_choice=int(input("What do you choose?Type 0 for rock,1 for paper or 2 for scissors.\n"))
if user_choice>=3 or user_choice<0:
     print("Out of scope,You lose!")
else:
     print(game_images[user_choice])

     computer_choice=random.randint(0,3)
     print(game_images[computer_choice])
     if user_choice==2 and computer_choice==0:
         print("You lose!")
     elif user_choice==0 and computer_choice==2:
         print("You win")
     elif user_choice>computer_choice:
         print("you win!")
     elif computer_choice>user_choice:
         print("You lose")
     elif user_choice==computer_choice:
         print("It's a draw")