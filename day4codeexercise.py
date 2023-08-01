import random
name_string=input("Give me everybody's names separated by comas.\n")
names=name_string.split(",")
#Get the total number of items the list
items_no=len(names)
#pick an item randomly
random_choice=random.randint(0,items_no-1)
person_who_will_pay=names[random_choice]
print(person_who_will_pay + " ""is going to buy the meal today.")

