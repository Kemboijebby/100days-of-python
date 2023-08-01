# def greet():
#     print("kemboi")
#     print("jebiwot")
#     print("anitah")
#greet()
#Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
# greet_with_name("anitah")

##function with more than one inputs
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Anitah","Finland")
#greet_with("finland","Anitah")...data interchanges and to overcome this we use keywords

#functions with keyword arguments
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with(name="Anitah",location="Finland")

#paint calculation
# import math
# def paint_calc(height,width,cover):
#     area=(height * width)
#     num_of_cans = math.ceil(area/cover)
#     print(f"you'll need {num_of_cans} cans of paint.")
# test_h=int(input("Height of the wall:"))
# test_w=int(input("Width of the wall:"))
# coverage=5
# paint_calc(height = test_h,width=test_w,cover=coverage)

#code exercise
#prime checker
# def prime_check(number):
#      is_prime=True
#      for i in range(2,number):
#          if number % i==0:
#              is_prime=False
#      if is_prime:
#          print("It is a prime number.")
#      else:
#          print("it is not a prime number")
#prime_check("number")

#CEASER CIPHER
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'
,'t','u','v','w','x','y','z''a','b','c','d','e','f','g','h','i','j','k,l','m','n','o','p','q','r','s'
,'t','u','v','w','x','y','z']
# direction = input("Type 'encode' to encrypt,type'decode'to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift=int(input("Type of shift number:\n"))

# def encrypt(plain_text,shift_amount):
#  cipher_text=""
#  for letter in plain_text:
#     position=alphabet.index(letter)
#     new_position=position + shift_amount
#     cipher_text+=alphabet[new_position]
#  print(f"The encoded text is {cipher_text}")
# encrypt(plain_text=text,shift_amount=shift)
# #incase we want to encode a message that is out of range we just duplicate the alphabet
# #decode
# def decrypt(cipher_text,shift_amount):
#   plain_text=""
#   for letter in cipher_text:
#     position=alphabet.index(letter)
#     new_position=position - shift_amount
#     plain_text+=alphabet[new_position]
#   print(f"The decoded text is {plain_text}")
# decrypt(cipher_text=text,shift_amount=shift)
#
# if direction=="encode":
#     encrypt(plain_text=text,shift_amount=shift)
# elif direction=="decode":
#     decrypt(cipher_text=text,shift_amount=shift)
def ceaser(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {cipher_direction}d text is {end_text}")
# from art import logo
# print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt,type'decode'to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type of shift number:\n"))

    shift= shift % 26
    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
    result = input("Type 'yes'if you want to go again.Otherwise type 'no'.\n")
    if result== 'no':
        should_continue = False
        print("Goodbye")