words_amount = int(input("Enter the amount of words: "))

if words_amount < 0:
    print ("Please enter a valid number")
else:
    words_list = []
    for i in range(words_amount):
        new_word = input(f"Enter the new word N°{i+1}: ")
        words_list.append(new_word)

    print("List of words:", words_list)

    replace_word = input("Enter a word to replace: ")
    replacement_word = input("Enter a replacement word: ")

    for i in words_list:
        if replace_word in words_list:
            index = words_list.index(replace_word) #index returns the value of wanted word
            words_list [index] = replacement_word #new value assigned to array
        else:
            print ("Invalid replacement, word was not found")
    
    print("The new word list is:", words_list)
