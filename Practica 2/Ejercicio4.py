words = int(input("Enter how many words you want in a list: "))
words_list = []

for i in range (words):
    word = str(input(f"Enter the word number {i+1}°: "))
    words_list += [word]
print(f"The created list is: {words_list}")

word_to_delete = str(input("Enter the word what you want to delete: "))

for index,element in enumerate(words_list):
    if element == word_to_delete:
        words_list.remove(word_to_delete)

print(f"The actual list looks like: {words_list}")