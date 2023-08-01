print("Welcome to tip calculator!")
bill=float(input("Total bill to be paid!"))
tip=int(input("what percentage tip would you like to give 10,12 or 15?"))
people=int(input("how many people are splitting this bill?"))
bill_with_tip=bill*(1+tip/100)
print(bill_with_tip)
each_person=float(bill_with_tip)/people
final_bill="{:.2f}".format(each_person)
print("Each person should pay"" "+str(final_bill))

