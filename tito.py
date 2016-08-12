import funciones

if __name__ == "__main__":
    manual = input('¿Desea cargar las comidas de forma manual? Y/N')
    if manual == 'Y' or manual == 'y':
        vector = funciones.crear_vector()
        funciones.cargar(vector)

    elif manual == "N" or manual == "n":
        vector = funciones.crear()
        funciones.cargar_aleatorio(vector)

funciones.mostrar_menu()

opcion =int(input("Ingrese la opcion deceada"))

while opcion != 7:
    funciones.mostrar_menu()
    opcion = int(input("Ingrese La opción deseada: "))

    if opcion == 1:
        funciones.mostrar_carta(vector)
        input("precione enter para continuar\n")

    elif opcion == 2:
        print("El Precio promedio es $",funciones.precio_promedio(vector))
        input("precione enter para continuar\n")

    elif opcion == 3:
        funciones.menor_tiempo_coccion(vector)
        input("precione enter para continuar\n")

    elif opcion == 4:
        funciones.comida_tipo()
        input("precione enter para continuar\n")

    elif opcion == 5:
        funciones.buscar_y_sugerir()
        input("precione enter para continuar\n")

    elif opcion == 6:
        funciones.menu_del_dia()
        input("precione enter para continuar\n")

    elif opcion == 7:
        print("¡Gracias por consultar nuestro menú!")
        break
