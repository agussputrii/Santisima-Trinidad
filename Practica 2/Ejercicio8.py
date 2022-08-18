words = int(input("Enter how many words you want in a list: "))
words_list1 = []

while words == 0 or words > 20:
    words = int(input("Please enter a valid number between 1 and 20: "))

for i in range (words):
    word = str(input(f"Enter the word N°{i+1}: "))
    words_list1.append(word)

removed_duplicates = set(words_list1)
words_list1 = list(removed_duplicates)

print(f"The created list is: {words_list1}")

#SECOND ARRAYLIST
words_list2 = []
words = int(input("Enter how many words you want in a list: "))

while words == 0 or words > 20:
    words = int(input("Please enter a valid number between 1 and 20: "))

for i in range (words):
    word = str(input(f"Enter the word N°{i+1}: "))
    words_list2.append(word)

removed_duplicates = set(words_list2)
words_list2 = list(removed_duplicates)

print(f"The created list is: {words_list2}")

#ACTIONS
common_words = []
for i in words_list1:
    if i in words_list2:
        common_words += [i]
print(f"Words in both lists are: {common_words}")

first_only = []
for i in words_list1:
    if i not in words_list2:
        first_only += [i]
print(f"words in FIRST LIST ONLY are: {first_only}")

second_only = []
for i in words_list2:
    if i not in words_list1:
        second_only += [i]
print(f"words in SECOND LIST ONLY are: {second_only}")

all_words = common_words + first_only + second_only
print(f"All words: {all_words}")



