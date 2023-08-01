#print(8//3)
#score=80
#height=1.5
#iswinning=True
#print(f"your score is {score},your height {height},your winning is {iswinning}")

age=input("what is your current age?\n")
maximum_age=90
age_as_int=int(age)
remaining=maximum_age-age_as_int
rem_as_int=int(remaining)
print("your remaining years are"" "+str(remaining))
days=rem_as_int*365
weeks=rem_as_int*52
months=rem_as_int*12
print(f"you have {days}days,{weeks}weeks,{months}months")
