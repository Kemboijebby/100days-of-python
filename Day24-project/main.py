# TODO: Create a letter using starting_letter.txt
PLACEHOLDER="[name]"
with open("invited_names.txt") as names_file:
    names=names_file.readlines()
    print(names)
with open("starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        print(new_letter)
        with open(f".././Day24-project/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)











