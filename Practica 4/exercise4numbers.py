# Escribir un programa que solicite el ingreso de una cantidad indeterminada
# de números mayores que 1, los agregamos a una lista y finalizando cuando se
# reciba un cero. Imprimir la cantidad de números primos ingresados y
# la cantidad de números negativos.

paid_numbers = []
odd_numbers = []
total_numbers = []
validation = True

print("Press 0 to exit\n")

while validation:
    numbers = (int(input("Enter a number: ")))
    total_numbers.append(numbers)
    if numbers % 2 == 0:
        paid_numbers.append(numbers)
    elif numbers % 2 != 0:
        odd_numbers.append(numbers)
    if numbers == 0:
        validation = False
        total_numbers.pop(-1)
        paid_numbers.pop(-1)

print ("Total numbers:",total_numbers)
print ("paid numbers:",paid_numbers)
print ("odd numbers:",odd_numbers)