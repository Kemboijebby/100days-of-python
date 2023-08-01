# #list comprehensions
# list=[1,2,3,3,4,5,6,7,8]
# new_list=[item for item in list] #do this

#conditional list comprehension;takes two conditional statements

import pandas

#NATO phonetic code words
data=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
word=input("Enter a word:").upper()
output_list=[phonetic_dict[letter] for letter in word]
print(output_list)