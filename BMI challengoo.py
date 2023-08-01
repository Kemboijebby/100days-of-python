#bmi challengeee
height=(input("Enter your height."))
weight=(input("Enter your weight."))
BMI=round(int(weight)/float(height)**2,2)
if BMI<18.5:
    print(f"Your BMI is {BMI},you are Underweight!")
elif BMI<25:
    print(f"Your BMI is {BMI},you have a Normal weight!")
elif BMI<30:
    print(f"Your BMI is {BMI},you are overweight!")
elif BMI<35:
    print(f"Your BMI is {BMI},you are obese!")
else:
    print(f"Your BMI is {BMI},you are clinically obese!")