import os
import random as rd
import csv

#1.	Registrar pedido
#Para registrar un pedido se requiere lo siguiente: Nombre y apellido del cliente, comuna, detalle del pedido. 
# Por ejemplo, la empresa vende dispensadores de 6, 10 y 20 litros. 
# Debe permitir ingresar la cantidad de cada cilindro a solicitar y considerar que la suma de 
# las cantidades (de cada cilindro) deben sumar más de cero (para que tenga sentido el pedido).
#Por lo tanto, un detalle de pedido podría verse registrado de la siguiente manera:


pedido = []

def id_pedido():
    id = rd.randint(100000, 999999)
    return id

def menu():
    while True:
        print("1.- Registrar pedido")
        print("2.- Listar todos los pedidos")
        print("3.- Imprimir hoja de ruta")
        print("4.- Buscar un pedido por ID")
        print("5.- Salir")
        opcion = input("Ingrese una opcion: ")
        os.system("cls")

        if opcion == "1":
            registrar_pedido()
            
        elif opcion == "2":
            listar()  

        elif opcion == "3":
            imprimir_hoja_ruta()    
        elif opcion == "4":
            buscar_por_id() 
        elif opcion == "5":
            break  

def registrar_pedido():
    dispensadores_6 = 0
    dispensadores_10 = 0
    dispensadores_20 = 0
    nombre = ""
    apellido = ""
    direccion = ""
    comuna = ""
    while nombre == "" and apellido == "" and comuna == "" and direccion == "":
       
        nombre = input("Ingrese Nombre: ")
        os.system("cls")
        apellido = input("Ingrese Apellido: ")
        os.system("cls")
        direccion = input("Ingrese Dirección: ").strip()
        os.system("cls")
        comuna = input("Ingrese Comuna: ") .strip()
        os.system("cls")
        try:        
            dispensadores_6 = int(input("Disp.6lts: "))
            os.system("cls")
        except ValueError:
            pass
        try:
            dispensadores_10 = int(input("Disp.10lts: "))
            os.system("cls")
        except ValueError:
            pass  
        try:
            dispensadores_20 = int(input("Disp.20lts: "))
            os.system("cls")
        except ValueError:
            pass    

        suma_dps = (dispensadores_6 + dispensadores_20 + dispensadores_10)
        if suma_dps > 0:
            

            pedidos = {
                "id": id_pedido(),
                "nombre": nombre,
                "apellido": apellido,
                "direccion": direccion,
                "comuna": comuna,
                "dispensadores_6": dispensadores_6,
                "dispensadores_10": dispensadores_10,
                "dispensadores_20": dispensadores_20
            }

            pedido.append(pedidos)
            
        else:
            print("Ingrese una cantidad valida de dispensadores.")
            
def listar():
    print("ID\tNombre\tApellido\tComuna\tDirección\tDisp.6lts\tDisp.10lts\tDisp.20lts")
    for i in pedido:
        print(f"{i['id']}\t{i['nombre']}\t{i['apellido']}\t{i['comuna']}\t{i['direccion']}\t{i['dispensadores_6']}\t{i['dispensadores_10']}\t{i['dispensadores_20']}")

def imprimir_hoja_ruta():
    print("Comuna\tDirección")
    for i in pedido:
        print(f"{i['comuna']}\t{i['direccion']}")
        
        generar_informe_ruta = input("Ingrese nombre de la dirección: ").strip()
        if i["direccion"] == generar_informe_ruta:
            with open("hoja_ruta.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Nombre", "Apellido", "Comuna", "Direccion", "Disp.6lts", "Disp.10lts", "Disp.20lts"])
                for i in pedido:
                    writer.writerow([i["id"], i["nombre"], i["apellido"], i["comuna"], i["direccion"], i["dispensadores_6"], i["dispensadores_10"], i["dispensadores_20"]])
  

def buscar_por_id():
    try:
        id = int(input("Ingrese el ID del pedido: "))
        for i in pedido:
            if i["id"] == id:
                print(f"ID: {i['id']}")
                print(f"Nombre: {i['nombre']}")
                print(f"Apellido: {i['apellido']}")
                print(f"Comuna: {i['comuna']}")
                print(f"Dirección: {i['direccion']}")
                print(f"Dispensadores 6lt: {i['dispensadores_6']}")
                print(f"Dispensadores 10lt: {i['dispensadores_10']}")
                print(f"Dispensadores 20lt: {i['dispensadores_20']}")                    
            else:
                print("Pedido no encontrado")
    except:
        print("Ingrese un ID valido")
menu()