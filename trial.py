MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def format_data(data):
    water=data['water']
    milk=data['milk']
    coffee=data['coffee']

    return (f"\nwater {water}ml"
            f"\nmilk {milk}ml"
            f"\ncoffee {coffee}g")

resource=format_data(resources)
print(resource)

# latte = MENU['latte']['ingredients']
# espresso = MENU['espresso']['ingredients']
# cappuccino = MENU['cappuccino']['ingredients']
#
# report={}
# def deal():
#
#     for key in resources:
#         if key in latte:
#             report[key]=resources[key]-latte[key]
#             print(report)
#         if key in espresso:
#             report[key] = resources[key] - espresso[key]
#             print(report)
#         if key in cappuccino:
#             report[key] = resources[key] - cappuccino[key]
#             print(report)
