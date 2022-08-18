# Escribir un programa que pida al usuario su peso (en kg)
# y estatura (en metros), calcule el índice de masa corporal y
# lo almacene en una variable, y muestre por pantalla la frase
# Tu índice de masa corporal es <imc> donde <imc> es el índice
# de masa corporal calculado redondeado con dos decimales. round(numero, 2) 

kg = float(input ("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))

bmi = kg / (height * height)

bmi = round(bmi,2)

print(f"Your body mass index is {bmi}")