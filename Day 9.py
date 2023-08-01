#Dictionaries and nested
# programming_dictionary = {
#     "Bug":"an error in a program that prevents the program from running as expected.",
#     "Function":"A piece of code that you can easily call over and over again.",
#     "Loop":"The action of doing something over and over again.",
# }
#Retrieving items from dictionary
#print(programming_dictionary[f"Function"])

#Adding new items to dictionary
#programming_dictionary["Stack"]="A linear data structure in which items inserted are removed in reverse order."

#print(programming_dictionary)
#wipe an existing dictionary

# programming_dictionary={}
# print(programming_dictionary)
#edit an item in a dictionary
# programming_dictionary["Bug"]="A moth in programming lingo."
# print(programming_dictionary)
#loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#grading exercise
# student_scores={
#     "Harry":81,
#     "Ron":78,
#     "Camille":99,
#     "MillyHilda":74,
#     "Bryson":62,
# }
# student_grades={}
# for student in student_scores:
#     score=student_scores[student]
#     if score >90:
#         student_grades[student]="Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)
#Nesting in Dictionaries and lists
# capitals = {
#     "france":"Paris",
#     "Germany":"Berlin"
# }
# #Nesting lists in a dictionary
# travel_log = {
#     "Kenya":{"cities_visited":["Nairobi","Eldoret","Nairobi"]},#dictionary in a dictionary
#     "Uganda":{"Towns_visited":["Kampala","Kagumo","Ruwenzori"],"total_visits": 12},
# }
# #nesting dictionary in a list
# travel_log=[{"Kenya":{"cities_visited":["Nairobi","Eldoret","Nairobi"]},#dictionary in a dictionary
#     "Uganda":{"Towns_visited":["Kampala","Kagumo","Ruwenzori"],"total_visits": 12},
#              }]

#CHALLENGE
# travel_log =[
#     {
#         "country":"France",
#         "visits":12,
#         "cities":["paris","lillie","Dijon"]
#     },
# {
#         "country":"Germany",
#         "visits":5,
#         "cities":["Berlin","Hamburg","Stuttgart"]
#     }
# ]
# def add_new_country(country_visited,times_visited,cities_visited):
#   new_country={}
#   new_country["country"]=country_visited
#   new_country["visits"]=times_visited
#   new_country["cities"]=cities_visited
#   travel_log.append(new_country)
# add_new_country("Russia",2,["moscow","saint petersburg"])
# print(travel_log)

#SECRET AUCTION PROGRAM
#from replit import clear
#from art import logo
bid={}

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount= bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid sh{highest_bid}")

bidding_finished= False
while not bidding_finished:
    name = input("What is your name?\n")
    price =int(input("What is your bid? sh\n"))
    bid[name] = price
    user_continue=input("Are their any other users?Type 'yes' or 'no'.\n").lower()
    if user_continue=="no":
        bidding_finished= True
        find_highest_bidder(bid)
    elif user_continue=="yes":
          bid={}




























