#Creamos nuestra clase bicicleteria
class Bicicleteria:

    def __init__(self):
        #lista para guardar bicicletas
        self.lista_bicicletas = []
        #variable de ganancias y cantidad de ventas
        self.ganancias = 0
        self.cantidad_de_ventas = 0

    #funcion para anadir bicicletas
    def anadir_bicicleta(self):

        print("\n---------------------------")
        print("Añadir bicicleta")
        print("---------------------------")
        #variables para guardar los datos de la bicicleta
        nro_de_serie = input("Ingrese el nro de serie de la bicicleta: ")
        modelo = input("Modelo de la bicicleta: ")
        anio = input("Año de la bicicleta: ")
        precio = input("Precio de la bicicleta: ")
        #añadimos la bicicleta creada a la lista
        self.lista_bicicletas.append({'numero de serie':nro_de_serie, 'modelo':modelo, 'anio':anio, 'precio':precio})
        print("Bicicleta añadida\n")
        return self.menu()

    #funcion para vender bicicletas
    def vender_bicicleta(self):
        print("\n---------------------------")
        print("Venta de bicicleta")
        print("---------------------------\n")
        #si no hay bicicletas
        if len (self.lista_bicicletas) == 0:
            print("No hay bicicletas")
        else:
            #mostramos las bicicletas
            for x in range(len (self.lista_bicicletas)):
                print(self.lista_bicicletas[x])
            n_serie = input("Ingrese el nro de serie de la bicicleta que desea vender: ")
            #recorremos la lista de bicicletas
            for x in range(len (self.lista_bicicletas)):
                if self.lista_bicicletas[x]['numero de serie'] == n_serie:#si encontramos la bicicleta que queremos vender
                    #guardamos el precio de la bicicleta
                    self.ganancias += int(self.lista_bicicletas[x]['precio'])
                    #guardamos la cantidad de ventas
                    self.cantidad_de_ventas += 1
                    #eliminamos la bicicleta de la lista
                    self.lista_bicicletas.remove(self.lista_bicicletas[x])
                    print("Bicicleta vendida")
                    return self.menu()

    #funcion para mostrar las bicicletas
    def mostrar_bicicletas(self):
        print("\n---------------------------")
        print("---------------------------\n")
        #si no hay bicicletas
        if len (self.lista_bicicletas) == 0:
            print("No hay bicicletas")
            return self.menu()
        else:
        #mostramos las bicicletas
            for x in range(len (self.lista_bicicletas)):
                print(self.lista_bicicletas[x])
        return self.menu()

    #funcion para ver las ganancias y cantidad de ventas
    def ganancias_y_ventas(self):
        print("\n--------------------------")
        print("Ganancias y ventas")
        print("--------------------------")
        print("Ganancias: $", self.ganancias)
        print("Ventas: [ ", self.cantidad_de_ventas, " ]")
        return self.menu()


    #funcion para revisar el precio de una bicicleta mediante su numero de serie
    def revisar_precio(self):
        print("\n---------------------------")
        print("Venta de bicicleta")
        print("---------------------------\n")
        #si no hay bicicletas
        if len (self.lista_bicicletas) == 0:
            print("No hay bicicletas")
            return self.menu()
        else:
            #mostramos las bicicletas
            for x in range(len (self.lista_bicicletas)):
                print(self.lista_bicicletas[x])
            n_serie = input("Ingrese el nro de serie de la bicicleta que desea ver su precio: ")
            #recorremos la lista de bicicletas y si la encontramos se realiza la modificacion
            for x in range(len (self.lista_bicicletas)):
                if self.lista_bicicletas[x]['numero de serie'] == n_serie:
                    print("Precio: $", self.lista_bicicletas[x]['precio'])
                else:
                    print("No se encontro la bicicleta")
                    return self.menu()

    def modificar_precio(self):
        print("\n---------------------------")
        print("Modificar precio")
        print("---------------------------\n")
        #si no hay bicicletas
        if len (self.lista_bicicletas) == 0:
            print("No hay bicicletas")
            return self.menu()
        else:
            for x in range(len (self.lista_bicicletas)):
                print(self.lista_bicicletas[x])
            n_serie = input("Ingrese el nro de serie de la bicicleta que desea modificar su precio: ")
            for x in range(len (self.lista_bicicletas)):
                #si encontramos la bicicleta que queremos modificar su precio:
                if self.lista_bicicletas[x]['numero de serie'] == n_serie:
                    precio = input("\nIngrese el nuevo precio: ")
                    self.lista_bicicletas[x]['precio'] = precio
                    print(f"Precio modificado\n")
                    return self.menu()
    #funcion string para mostrar la lista de bicicletas
    def __str__(self):
        return str(self.lista_bicicletas)


    def menu(self):
        print("\n---------------------------")
        print("             MENU             ")
        print("==============================")
        print("1. Añadir bicicleta")
        print("2. Mostrar bicicletas")
        print("3. Vender bicicleta")
        print("4. Mostrar ganancias y ventas")
        print("5. Revisar precio")
        print("6. Modificar precio")
        print("7. Salir")
        print("---------------------------")
        opcion = input("Ingrese una opcion: ")
        #segun la opcion se llama a una funcion
        if opcion == "1":
            self.anadir_bicicleta()
        elif opcion == "2":
            self.mostrar_bicicletas()
        elif opcion == "3":
            self.vender_bicicleta()
        elif opcion == "4":
            self.ganancias_y_ventas()
        elif opcion == "5":
            self.revisar_precio()
        elif opcion == "6":
            self.modificar_precio()
        elif opcion == "7":
            print("\nGracias por utilizar nuestro sistema")
            return False
        else:
            print("\nOpcion no valida")#si no se ingresa una opcion valida se vuelve al menu
            return self.menu()

class Bicicleta(Bicicleteria):
    def __init__(self,nro_de_serie, modelo, anio, precio):
        self.nro_de_serie = "numero de serie: "
        self.modelo = "modelo: "
        self.anio = "anio: "
        self.precio = "precio: "

    def get_precio(self):
        return self.precio
    
    def set_precio(self, precio):
        self.precio = precio

    def get_nro_de_serie(self):
        return self.nro_de_serie

    def __str__(self):
        return f"{self.nro_de_serie},{self.modelo},{self.anio},{self.precio}"

b1 = Bicicleta(123, "BMX", 2019, 100)
b2 = Bicicleta(456, "Trek", 2020, 200)
b3 = Bicicleta(789, "Scott", 2021, 300)
b4 = Bicicleta(321, "Specialized", 2022, 400)
lista_bicicletas = [b1, b2, b3, b4]

bicicleteria1 = Bicicleteria()
bicicleteria1.menu()


