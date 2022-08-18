# Una panadería vende barras de pan a 35$ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que
# se le hace por no ser fresca y el coste final total.

bread = float(input("Enter the number of breads than aren't of today: "))

discount = 0.6
price = 35
cost = bread * price  * (1 - discount)

print(f"The price of fresh bread is ${price}")

print(f"The price of ¨old¨ bread is ${(discount * 100)}")

print(f"The price to pay is ${round(cost,2)}")