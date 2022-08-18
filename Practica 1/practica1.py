print ("Holi mundo uwu")

# esto es una cadena
c = "odnum aloh"

# esto un entero
e = 23

#podemos comprobarlo con la funcion type
type (c)
type (e)
print (type (c)); print (type (e))

#para representar numeros reales:
real = 12.392
#También se puede utilizar notación científica
real = 2.1e-3

#numeros complejos en Python
complejo = 2.1 + 5.4j

#OPERADORES ARITMETICOS

#- Negación r = -7 # r es -7
#* Multiplicación r = 2 * 6 || r = 12
#** Exponente r = 2 ** 6 || r = 64
#/ División r = 3.5 / 2 || r = 1.75
#// División entera r = 3.5 // 2 || r = 1.0
#% Módulo r = 7 % 2 || r = 1

triple = """primera linea
esto se vera en otra linea"""

print (triple)

#CONECATENAR CADENAS

# a = “uno”
# b = “dos”
# c = a + b # c = “unodos”
# c = a * 3 # c = “unounouno”


#BOOLEANOS

# and ¿se cumple a y b? r = True and False # r = False
# or ¿se cumple a o b? r = True or False # r = True
# not No a r = not True # r = False

# == ¿son iguales a y b? r = 5 == 3 # r = False
# != ¿son distintos a y b? r = 5 != 3 # r = True
# < ¿es a menor que b? r = 5 < 3 # r = False
# > ¿es a mayor que b? r = 5 > 3 # r = True
# <= ¿es a menor o igual que b? r = 5 <= 5 # r = True
# >= ¿es a mayor o igual que b? r = 5 >= 3 # r = True

#LISTAS
print ('LISTAS')

l = [22, True, "elemento de una lista", [1, 2]]

print (l)
print (l[2])
#Seleccionar elemento de una lista
#y asociarlo a otra variable
r = l [3]
print (r)

l2 = ["una lista", [1, 2]] 
r2 = l2 [1][0] # r va a ser igual a 1
print (r2)

#modificar lista
l3 = [22, False]
print (l3)
l3 [0] = "Cambiamos el 22 por una cadena str"
print (l3)

#con [-1] accedemos al elemento final de la lista
print(l[-1])

