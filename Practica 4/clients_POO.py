def add_client (clients):
    print("adding client:\n")
    dni = input("DNI: ")
    name = input("Name: ")
    adress = input("Address: ")
    telephone = input("Telephone: ")
    email = input("Email: ")
    vip = input("¿Vip?(y/n): ")

    client ={
        "name": name,
        "adress": adress,
        "telephone": telephone,
        "email": email,
        "vip": vip == "y"
    }
    clients[dni] = client
    return

def client_modify():
    if len(clients) == 0:
        print("No clients")
    else:
        print("\nModify client:\n")
        dni = input("DNI of client to modify: ")
        if dni in clients:
            print("\nClient found:\n")
            for k,v in clients.items():
                if k == dni:
                    for k,v in v.items():
                        print(f"{k.capitalize()}: {v}")
            print()
            name = input("New name: ")
            adress = input("New adress: ")
            telephone = input("New telephone: ")
            email = input("New email: ")
            vip = input("¿Vip?(s/n): ")
            client = {
                "name": name,
                "adress": adress,
                "telephone": telephone,
                "email": email,
                "vip": vip == "s"
            }
            clients[dni].update(client)
        else:
            print("Client not found")
    return

def client_delete(clients):
    if len(clients) == 0:
        print("No clients")
        return
    else:
        print("\nDelete client:\n")
        dni = input("DNI of client to delete: ")
        if dni in clients:
            print("\nClient found:\n")
            if dni in clients():
                del clients[dni]
                print("\nClient deleted")
        else:
            print("Client not found")
    return

def client_list(clients, vip = False):
    if len(clients) == 0:
        print("No clients")
    elif vip == True:
        print("\nList of VIP clients:\n")
        for dni,data in clients.items():
            if data["vip"] == True:
                print(data["name"])
    else:
        print("\nList of clients:\n")
        for dni,data in clients.items():
            print(data["name"])
    return

def menu(clients):
    while True:
        menu = ("\nMenu:\n"
                + "1. Add client\n"
                + "2. Modify client\n"
                + "3. Delete client\n"
                + "4. List of clients\n"
                + "5. List of VIP clients\n"
                + "0. Exit\n"
                + "Choose one option: "
        )
        option = input(menu)
        if option == "1":
            add_client(clients)
        elif option == "2":
            client_modify(clients)
        elif option == "3":
            client_delete(clients)
        elif option == "4":
            client_list(clients)
        elif option == "5":
            client_list(clients, vip = True)
        elif option == "0":
            break
        else:
            continue
    return

def main():
    clients = {}
    menu(clients)
    print ("\nBye")
    return

main()