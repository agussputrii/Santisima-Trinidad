# Codear un programa que le permita crear una lista de palabras y
# que luego le pida 2 palabras y reemplace la primera palabra por
# la segunda en la lista.

words = int(input("Enter how many words you want in a list: "))
words_list = []

for i in range (words):
    word = str(input(f"Enter the word number {i+1}°: "))
    words_list += [word]
print(f"The created list is: {words_list}")

word_to_replace = str(input("Enter a word would you like to replace: "))
replaced_word = str(input("Enter the new word: "))

for index,element in enumerate (words_list):
    if element == word_to_replace:
        words_list [index] = replaced_word
        print("word to replace was found in position ",(index+1))
        break
    else:
        print("The value",word_to_replace,"wasn't found in the position",(index+1))

print(f"The final list: {words_list}")




