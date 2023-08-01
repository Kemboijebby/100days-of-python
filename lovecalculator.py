print("Welcome to LOVE calculator.")
name1=input("what's your name?\n")
name2=input("what's your partners name?\n")

combined_name=name1 + name2
lower_case_combination=combined_name.lower()

t=lower_case_combination.count("t")
r=lower_case_combination.count("r")
u=lower_case_combination.count("u")
e=lower_case_combination.count("e")
true=t+r+u+e

l=lower_case_combination.count("l")
o=lower_case_combination.count("o")
v=lower_case_combination.count("v")
e=lower_case_combination.count("e")
love=l+o+v+e

love_score=int(str(true)+str(love))
if (love_score<10) or (love_score>90):
    print(f"your love_score is {love_score},you go together like coke and mentos!")
elif (love_score>=40) and (love_score<=50):
    print(f"your love_score is {love_score},you guys are alright together!")
else:
    print(f"your love_score is {love_score},NEGATIVE!!!!")
