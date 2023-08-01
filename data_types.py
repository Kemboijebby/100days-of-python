print("hello"[4])
print(123+456)
print("123"+"456")
#type checking
num_char="kemboi"
print(type(num_char))

#type conversion
#num_char=len(input("whats your name?"))
#new_num_char=str(num_char)
#print("your name has"" "+new_num_char+ " ""characters")

num=input("Enter a two digit number.")
#print(type(num))
first_digit=(num[0])
second_digit=(num[1])
result=int(first_digit)+int(second_digit)
print(result)