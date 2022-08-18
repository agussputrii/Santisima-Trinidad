num = int(input(("How many people you want in a list?")))
names = []

for i in range (0,num):
    name = input(f"Enter the {i+1}° name: ")
    names += [name]

print(f"The result of your list is {names}")
