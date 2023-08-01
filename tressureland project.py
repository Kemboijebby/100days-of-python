print("Welcome to treasure land.")
print("Your work is to find the treasure.")
choice1=input('You\'re at a crossroad,where do you want to go?Type "left"or "Right."\n').lower()

if choice1 == "Left":
  choice2 = input('You\'ve come to a lake.There is an island in the middle of the lake.Type "wait"to wait for a boat.Type"swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input('you arrived at the island unharmed.There is a house with three doors.one yellow,one red,one blue.Which door do you choose?\n.').lower()
    if choice3 == "Red":
          print("It is room full of fire.Game over.")
    elif choice3 == "yellow":
          print("You found the treasure.You win.")
    elif choice3 == "blue":
          print("you entered a room full of beasts.Game over.")
    else:
          print("You chose a door that does not exist.Game over.")
  else:
      print("You got attacked by an angry crocodile.Game over.")
else:
    print("You fall into a hole.Game over.")