import datetime

inputDate=input("Enter the date in the format 'yy/mm/dd/':")
year,month,day=inputDate.split('/')
def is_valid_date():
    date=inputDate
    if date:
        try:
            datetime.datetime(int(year),int(month),int(day))
            print("Input date is valid.")
        except ValueError:
            print("Input date is not valid")




is_valid_date()