#Importamos modulo
import math

#Codigo
opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los números
    5) Potenciarr los números
    6)Raiz...
    """)
    opcion = int(input("Elige una opción: ") )     

    #Suma
    if opcion == 1:
        print("---------------------------------------")
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print("=======================================")
        suma = n1 + n2
        print(f"El resultado de tu suma es => {suma}") 
    
    #Resta
    if opcion == 2:
        print("---------------------------------------")
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        print("=======================================")
        resta = n1 - n2
        print(f"El resultado de tu resta es => {resta}")
    
    #Multiplicación
    if opcion == 3:
        print("---------------------------------------")
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        multiplicación = n1 * n2
        print("=======================================")
        print(f"El resultado de tu multiplicación es {multiplicación}")
    
    #División
    if opcion == 4:
        print("---------------------------------------")
        n1 = float(input("Introduce tu primer número: ") )
        n2 = float(input("Introduce tu segundo número: ") )
        division = n1 / n2
        print("=======================================")
        print(f"El resultado de tu división es {division}")

    #Potenciación
    if opcion == 5:
        print("---------------------------------------")
        n1 = float(input("Introduce la base: ") )
        n2 = float(input("Introduce la potencia: ") )
        potenciacion = n1 ** n2 
        print("=======================================")
        print(f"El resultado de la potenciación es {potenciacion}")
    

        
