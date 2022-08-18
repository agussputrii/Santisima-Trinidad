#Escribir un programa que lea un entero positivo n
#introducido por el usuario y después muestre en 
#pantalla la suma de todos los enteros desde 
#1 hasta n. La suma de los n primeros enteros 
#positivos puede ser calculada de la siguiente forma:
  
num = int(input("enter an integer: "))

total = num * (num +1) / 2

print(f"the sum of the integers up to {num} is {total}")