#functions with output
#convert string to title case
# def format_name(f_name, l_name):
#     formated_f_name=f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name},{formated_l_name}"
# print(format_name("anItAH","KeMbOi"))

# def format_name(f_name, l_name):
#      if f_name=="" or l_name=="":
#        return "You didn't provide valid inputs."
#      formated_f_name=f_name.title()
#      formated_l_name = l_name.title()
#      return f"Result:{formated_f_name},{formated_l_name}"
# print(format_name(input("what is your first name?"),input("what is your last name?")))


#print(type(Year))
# def is_leap(Year):
#     if Year%4==0:
#         if Year%100==0:
#             if Year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#        return False
# def days_in_month(Year,month):
#     month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if is_leap(Year) and month==2:
#         return 29
#     return month_days[month-1]
# Year=int(input("Enter a year"))
# month=int(input("Enter a month"))
# days=days_in_month(Year,month)
# print(days)

#calculator
#add
from art import logo
def add(n1,n2):
    return n1 + n2

#subtact
def subtract(n1,n2):
    return n1 - n2

#multiply
def multiply(n1,n2):
    return n1 * n2

#divide
def divide(n1,n2):
    return n1/n2
def calculator():
    print(logo)
    operations={"+":add,"-":subtract,"*":multiply,"/":divide}
    num1=float(input("what's the first number?:"))
    num2=float(input("what's the second number?:"))

    for symbol in operations:
        print(symbol)
    operation_symbol=input("pick an operation from the line above:")
    calculation_function = operations[operation_symbol]
    first_answer=calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    should_continue=True
    while should_continue:
        operation_symbol=input("pick another operation:")
        num3=int(input("what's the next number?:"))
        #second_answer=""
        #continue_op=input(f"Type 'y' to continue calculating with {second_answer},or 'n'to ")
        calculation_function=operations[operation_symbol]
        second_answer=calculation_function(first_answer,num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

        if input(f"type 'y'to continue calculating with {second_answer}, or type 'n' to start a new calculation.:") =="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()














