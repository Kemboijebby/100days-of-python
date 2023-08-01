#print(3*3+3/3-3)

#BMI
height=input("Enter your height in m\n")
weight=input("enter your weight in kgs\n")
BMI=int(weight)/float(height)**2
BMI_as_int=int(BMI)
print("Your BMI is"" "+str(BMI_as_int))