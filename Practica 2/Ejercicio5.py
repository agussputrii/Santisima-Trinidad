words = int(input("Enter how many words you want in a list: "))
words_list = []

while words == 0 or words > 20:
    words = int(input("Please enter a valid number between 1 and 20: "))

for i in range (words):
    word = str(input(f"Enter the word N°{i+1}: "))
    words_list += [word]
print(f"The created list is: {words_list}")

del_words = int(input("How many words you do like to delete from the list above: "))
del_words_list = []

for i in range(del_words):
    del_word = str(input(f"Enter the word N°{i+1}: "))
    del_words_list += [del_word]

for i,elem in enumerate(words_list):
    for j,elem2 in enumerate(del_words_list):
        if words_list [i] == del_words_list[j]:
            words_list.pop(i)



print(f"The created list is: {words_list}")