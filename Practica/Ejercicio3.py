#Escribir un programa que pregunte al usuario
#por el número de horas trabajadas y el coste
#por hora. Después debe mostrar por pantalla
#la paga que le corresponde.

salary = int(input("Enter your salary: $"))

workedTime = int(input("Enter the total of time worked: "))

total = salary * workedTime

print(f"Your total salary is ${total}")