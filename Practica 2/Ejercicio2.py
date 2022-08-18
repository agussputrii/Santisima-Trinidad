# Codear un programa que le permita crear una lista de palabras y
# que, a continuación, pida una palabra y diga cuántas veces
# aparece la misma dentro de la lista.

number = int(input("Enter how many words you want in a list: "))

names_list = []

for i in range (number):
    name = str(input(f"Enter the word number {i+1}°: "))
    names_list += [name]
print(f"The created list is: {names_list}")

search = str(input("Enter the word what u want to search in the list: "))
count = names_list.count(search)

print("The world",search, "appears",count, "times")
