# import random
# dice_imgs = ["1","2","3","4","5"]
# dice_num = random.randint(0,4)
# print(dice_imgs[dice_num])
#
# year=int(input("What is your year of birth?"))
# if year>=1980 and year<=1994:
#     print("you are a millenian.")
# elif year>1994:
#     print("You're a Gen Z.")


# pages=0
# word_per_page=0
# pages=int(input("Number of pages:"))
# word_per_page=int(input("Number of words per page:"))
# print(f"pages={pages}")
# print(f"word_per_page={word_per_page}")
# total_words=pages*word_per_page
# print(total_words)

# def mutate(a_list):
#     b_list=[]
#     for item in a_list:
#         new_item=item *2
#         b_list.append(new_item)
#     print(b_list)
# mutate([1,2,3,4,5,6])

# year=int(input("which year do you want to test?"))
# if year % 4==0:
#     if year % 100==0:
#         if year % 400==0:
#             print("leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("leap year")
# else:
#     print("Not leap year")

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number %3==0:
        print("Buzz")
    elif number % 5==0:
        print("fizz")
    else:
        print(number)

# for number in range(1,101):
#     if number % 11==0:
#         print(number)
#     else:
#         print("Not divisible")
