words_amount = int(input("Enter the amount of words: "))

if words_amount < 0:
    print ("Please enter a valid number")
else:
    words_list = []
    for i in range(words_amount):
        new_word = input(f"Enter the word number {i+1}: ")
        words_list.append(new_word)

    print(f"The final list is:\n",words_list)