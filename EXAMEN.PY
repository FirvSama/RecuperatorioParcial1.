nombres = []
cantidades = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            break
        except ValueError:
            print("Por favor, ingrese un numero válido.")
    nombres.append(nombre)
    cantidades.append(cantidad)
    print(" Producto agregado con éxito.  ")

def ver_productos_agotados():
    agotados = False
    print(" Productos agotados:")
    for i in range(len(nombres)):
        if cantidades[i] == 0:
            print(f"- {nombres[i]}")
            agotados = True
    if not agotados:
        print("No hay productos agotados.  ")

def actualizar_stock():
    producto = input("Ingrese el nombre del producto a actualizar: ")
    if producto in nombres:
        indice = nombres.index(producto)
        while True:
            try:
                nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
                break
            except ValueError:
                print("Por favor, ingrese un numero válido.")
        cantidades[indice] = nueva_cantidad
        print(" Stock actualizado.  ")
    else:
        print(" Producto no encontrado.  ")

def ver_todos_los_productos():
    print(" Listado de productos:")
    for i in range(len(nombres)):
        print(f"- {nombres[i]}: {cantidades[i]} unidades")
    print()

def mostrar_menu():
    print(" MENU DE OPCIONES")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

# Programa principal
salir = False
while not salir:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")
    print()
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_productos_agotados()
    elif opcion == "3":
        actualizar_stock()
    elif opcion == "4":
        ver_todos_los_productos()
    elif opcion == "5":
        print(" Gracias por usar el sistema.")
        salir = True
    else:
        print(" Opcion invalida. Intente nuevamente.  ")
