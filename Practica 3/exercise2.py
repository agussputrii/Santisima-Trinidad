words_amount = int(input("Enter the amount of words: "))

if words_amount < 0:
    print ("Please enter a valid number")
else:
    words_list = []
    for i in range(words_amount):
        new_word = input(f"Enter the new word N°{i+1}: ")
        words_list.append(new_word)

    print("List of words:", words_list)

    search_word = str(input("Enter a word to count how many times it appears in the list: "))
    count_word = words_list.count(search_word)

    print(f"The word '{search_word}' appears {count_word} times in the list.")