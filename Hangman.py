#step 1
#generate a random word
end_of_game = False
word_list=["paranoia","monkey","camel"]
#TODO-1-Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosen_word=random.choice(word_list)
print(f"The chosen word is {chosen_word}")

#TODO-1-Create a variabe called lives to keep track  of the nimber of lives left
lives=""

#TODO-i-create an empty list calle display
#TODO-ii-for each letter in chosen_word ,add a "_" to display
display=[]
word_length=len(chosen_word)
for letter in chosen_word:
    display +="_"
print(display)

end_of_game = False

while not end_of_game:
    #TODO-2-Ask the user to guess a letter and assign their answer to a variable called guess .make guess lowercase
    guess=input("Guess a letter:").lower()
    #TODO-3-Check if the guessed(guess) is one of the words in the chosen_word
    if guess in display:
        print(f"you\'ve already guessed {guess}")
    #TODO-iii-loop through each position of the chosen_word
    for position in range(word_length):
        letter=chosen_word[position]
       # print(f"current position:{position}\ncurrent letter:{letter}\nGuessed letter:{guess}")
        if letter==guess:
            display[position]=letter

    if guess not in chosen_word:
       print(f"you guessed {guess},that is not in the word,you lose a life.")
       lives -= 1
       if lives == 0:
           end_of_game= True

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")

#Todo...insert the ASCCI Art
    #print(stages[lives])




















