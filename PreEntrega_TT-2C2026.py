#Pre-entrega: Sistema de gestion de productos
#Cada producto es una sublista de 3 elementos: [nombre, categoria, precio]

productos = [] #lista principal, aca se guardan todas las sublistas de productos

#Menu principal, se repite hasta que se elija la opcion de salir
while True:
    print("\n=============== GESTIÓN DE PRODUCTOS ===============")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Elija una opción: ").strip() #strip() elimina los espacios al inicio y al final

    #AGREGAR PRODUCTO
    if opcion == "1":
        #Valido que el nombre no este vacio, se vuelve a pedir hasta que ingrese algo
        nombre = input("Ingrese el nombre: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre: ").strip()

        categoria = input("Ingrese la categoría: ").strip()
        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría: ").strip()

        #isdigit() solo acepta numeros enteros, asi no se pueden poner centavos, letras ni negativos
        precio = input("Ingrese el precio (sin centavos): ").strip()
        while not precio.isdigit() or int(precio) == 0: #si no es digito, el or ya da True y no llega al int()
            print("Precio inválido, ingrese un número entero mayor a 0.")
            precio = input("Ingrese el precio (sin centavos): ").strip()
        precio = int(precio) #el int va despues de validar para evitar errores

        productos.append([nombre, categoria, precio]) #agrego la sublista al final de la lista
        print(f"Producto '{nombre}' agregado correctamente.")

    #VER PRODUCTOS
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\n------------- PRODUCTOS REGISTRADOS -------------")
            for i in range(len(productos)): #recorro por indice para poder numerar cada producto
                print(f"{i + 1}. Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: ${productos[i][2]}")
                #productos[i][0] => primer elemento de la sublista que esta en la posicion i

    #BUSCAR PRODUCTO
    elif opcion == "3":
        if len(productos) == 0:
            print("\n------------- PRODUCTOS -------------")
            print("No hay productos registrados.")
        else:
            busqueda = input("Ingrese el nombre a buscar: ").strip()
            while busqueda == "":
                print("La búsqueda no puede estar vacía.")
                busqueda = input("Ingrese el nombre a buscar: ").strip()

            encontrado = False #si no cambia a True en el for, no hubo coincidencias
            print("\n------------- RESULTADOS -------------")
            for i in range(len(productos)):
                #lower() en los dos lados para que no importen mayusculas/minusculas
                #in busca si el texto esta dentro del nombre, asi "manga" encuentra "Manga One Piece"
                if busqueda.lower() in productos[i][0].lower():
                    print(f"{i + 1}. Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: ${productos[i][2]}")
                    encontrado = True

            if not encontrado:
                print(f"No se encontraron resultados para '{busqueda}'.")

    #ELIMINAR PRODUCTO
    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            #Muestro la lista para que se sepa que numero tiene cada producto
            print("\n------------- PRODUCTOS REGISTRADOS -------------")
            for i in range(len(productos)):
                print(f"{i + 1}. Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: ${productos[i][2]}")

            numero = input("Ingrese el número del producto a eliminar (0 para cancelar): ").strip()
            while not numero.isdigit() or int(numero) > len(productos): #no puede ser mayor a la cantidad de productos
                print(f"Número inválido, ingrese un número entre 1 y {len(productos)} (0 para cancelar).")
                numero = input("Ingrese el número del producto a eliminar (0 para cancelar): ").strip()
            numero = int(numero)

            if numero == 0:
                print("Eliminación cancelada.")
            else:
                eliminado = productos.pop(numero - 1) #-1 porque la lista empieza en 0 y la numeracion en 1, pop devuelve lo que elimina
                print(f"Producto '{eliminado[0]}' eliminado correctamente.")

    #SALIR
    elif opcion == "5":
        print("Saliendo del sistema...")
        break #rompe el while True y termina el programa

    else:
        print("Opción no válida, elija un número del 1 al 5.")
