#creamos clase bicicleta
class Bicicleta:
    #constructor
    def __init__(self, nro_de_serie, modelo, anio, precio):
        self.nro_de_serie = nro_de_serie
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    #getters y setters
    def get_precio(self):
        return self.precio

    def get_nro_de_serie(self):
        return self.nro_de_serie  

    def set_precio(self, precio):
        self.precio = precio

    #funcion string para mostrar la lista de bicicletas
    def __str__(self):
        return f"\nn° de serie: {self.nro_de_serie}, modelo: {self.modelo}, año: {self.anio}, precio: ${self.precio}"


#creamos clase bicicleteria
class Bicicleteria:
    #constructor
    def __init__(self):
        self.lista_bicis = []
        self.ganancias = 0
        self.cantidad_de_ventas = 0
        print("Bicicleteria creada")

#1
    #funcion para crear bicicleta
    def crear_bici(self):
        print("\n---------------------------")
        print("Añadir bicicleta")
        print("---------------------------")
        #variables para guardar los datos de la bicicleta
        nro_de_serie = (input("Ingrese el nro de serie: "))
        modelo = input("Ingrese el modelo: ")
        anio = int(input("Ingrese el año: "))
        precio = float(input("Ingrese el precio: "))
        bici = Bicicleta(nro_de_serie, modelo, anio, precio)
        self.ingresar_bici(bici)
        return self.menu()

    #funcion para ingresar una bicicleta a la lista
    #utilizada en la funcion crear_bici
    def ingresar_bici(self, Bicicleta):
        self.lista_bicis.append(Bicicleta)
        for bici in self.lista_bicis:
            print(bici)
        return self.menu()

#2
    #funcion para mostrar bicicletas con return al menu
    def mostrar_bicis(self):
        print("\n---------------------------")
        for i in range(len(self.lista_bicis)):
            print(f"{i+1}. {self.lista_bicis[i]}")
        return self.menu()

    #funcion para listar bicicletas a modo de void
    def listar_bicis(self):
        print("\n---------------------------")
        for i in range(len(self.lista_bicis)):
            print(f"{i+1}. {self.lista_bicis[i]}")

#3
    #funcion para vender bicicleta
    def vender_bici(self):
        print("\n---------------------------")
        print("Vender bicicleta")
        print("---------------------------\n")
        #si no hay bicicletas
        if len(self.lista_bicis) == 0:
            print("No hay bicicletas")
            return self.menu()
        #si hay bicicletas mostramos
        self.listar_bicis()
        #pedimo el nro de serie
        nro_de_serie = (input("\nIngrese el nro de serie: "))
        #recorremos la lista de bicicletas
        for bici in self.lista_bicis:
            #si se encuentra la bicicleta
            if bici.get_nro_de_serie() == nro_de_serie:
                #se le suma a ganancia el precio de la bicicleta
                self.ganancias += bici.get_precio()
                #se le suma a cantidad de ventas una unidad
                self.cantidad_de_ventas += 1
                #finalmente se elimina la bicicleta de la lista
                self.lista_bicis.remove(bici)
                print("\nBicicleta vendida")
                return self.menu()


#4
    #funcion para mostrar ganancias y cantidad de ventas
    def ganancias_y_ventas(self):
        print("\n---------------------------")
        print("Ganancias y ventas")
        print("---------------------------")
        print(f"Ganancias: ${self.ganancias}")
        print(f"Ventas: {self.cantidad_de_ventas}")
        return self.menu()

#5
    #funcion para revisar el precio de una bicicleta mediante el nro de serie
    def revisar_precio(self):
        #si no hay bicicletas
        if len(self.lista_bicis) == 0:
            print("No hay bicicletas")
            return self.menu()
        #si hay bicicletas mostramos
        self.listar_bicis()
        nro_de_serie = input("Ingrese el nro de serie: ")
        for bici in self.lista_bicis:
            if bici.get_nro_de_serie() == nro_de_serie:
                print(f"\nPrecio: {bici.get_precio()}")
                return self.menu()
            else:
                print("Bicicleta no encontrada")
                return self.menu()

#6  
    #modificar precio
    def modificar_precio(self):
        print("\n---------------------------")
        print("Modificar precio")
        print("---------------------------\n")
        #si no hay bicicletas
        if len(self.lista_bicis) == 0:
            print("No hay bicicletas")
            return self.menu()
        #si hay bicicletas mostramos
        else:
            self.listar_bicis()
            nro_de_serie = (input("Ingrese el nro de serie: "))
            for bici in self.lista_bicis:
                if bici.get_nro_de_serie() == nro_de_serie:
                    #pedimos el nuevo precio
                    precio = float(input("Ingrese el nuevo precio: "))
                    #seteamos el nuevo precio
                    bici.set_precio(precio)
                    print("Precio modificado")
                    return self.menu()
                else:
                    continue
        return self.menu()

#7
    #metodo opcional para precargar la lista de bicicletas
    def precargar_bicis(self):
        bici_1 = Bicicleta("123", "BMX", 2019, 100)
        bici_2 = Bicicleta("456", "Trek", 2020, 200)
        bici_3 = Bicicleta("789", "Scott", 2021, 300)
        bici_4 = Bicicleta("321", "Specialized", 2022, 400)
        self.lista_bicis.append(bici_1)
        self.lista_bicis.append(bici_2)
        self.lista_bicis.append(bici_3)
        self.lista_bicis.append(bici_4)
        print("\nBicicletas precargadas con exito")
        return self.menu()

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
        print("7. Precargar bicicletas")
        print("8. Salir")
        print("---------------------------")
        opcion = input("Ingrese una opcion: ")
        #segun la opcion se llama a una funcion
        if opcion == "1":
            return self.crear_bici()
        elif opcion == "2":
            return self.mostrar_bicis()
        elif opcion == "3":
            return self.vender_bici()
        elif opcion == "4":
            return self.ganancias_y_ventas()
        elif opcion == "5":
            return self.revisar_precio()
        elif opcion == "6":
            return self.modificar_precio()
        elif opcion == "7":
            return self.precargar_bicis()
        elif opcion == "8":
            print("Gracias por usar nuestra bicicleteria")
            return False
        else:
            print("Opcion invalida")
            return self.menu()

#funcion main
def main():
    bicicleteria = Bicicleteria()
    bicicleteria.menu()

#ejecutamos main
main()
