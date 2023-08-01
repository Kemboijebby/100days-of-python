# file = open("my_file.txt")
# contents=file.read()
# print(contents)
# file.close()


#with is used when you do want to use the close method
#read mode
# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)

#write mode
#write mode also creates a new file when a file doesn't exist
# with open("my_file.txt",mode="w") as file:
#     file.write("\n I'm a junior data scientist.")

#append mode
with open("my_file.txt",mode="a") as file:
    file.write("\nI'm a python programmer too")