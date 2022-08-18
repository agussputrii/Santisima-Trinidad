words = int(input("Enter how many words you want in a list: "))
words_list = []

while words == 0 or words > 20:
    words = int(input("Please enter a valid number between 1 and 20: "))

for i in range (words):
    word = str(input(f"Enter the word N°{i+1}: "))
    words_list.append(word)

print(f"The created list is: {words_list}")

reversed_words_list = []

for i in enumerate(words_list):
    reversed_words_list = words_list [::-1]
    
print(f"The inverted list is: {reversed_words_list}")