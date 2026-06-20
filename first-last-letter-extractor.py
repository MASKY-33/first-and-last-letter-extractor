## This Program:
# - asks a word
# - takes first and last letter (indexing)
# - prints first and last letter of the given word

give_word = input("Type a word: ")

first_letter = (give_word[0])
last_letter = (give_word[-1])
print(f"({first_letter}) ({last_letter})")
