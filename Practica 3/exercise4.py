words_amount = int(input("Enter the amount of words: "))

if words_amount < 0:
    print ("Please enter a valid number")
else:
    words_list = []
    for i in range(words_amount):
        new_word = input(f"Enter the new word N°{i+1}: ")
        words_list.append(new_word)

    print("List of words:", words_list)

    delete_word = input("Enter the word to delete in the last array: ")

    for i in words_list:
        if delete_word in words_list:
            words_list.remove(delete_word)
    print("The new word list is:", words_list)