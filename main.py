# coding:utf-8
import funciones


def mostrar_menu():
    print("1)Consultar carta: ")
    print("2)Calcular precio promedio: ")
    print("3)Buscar comida con menor tiempo de cocción: ")
    print("4)Calcular y mostrar la cantidad de comidas por tipo: ")
    print("5)Buscar en la carta un plato principal: ")
    print("6)Mostrar el menu del día completo: ")
    print("7)Salir")
    print()


opcion = 0

if __name__ == "__main__":
    manual = str(input('¿Desea cargar las comidas de forma manual? Y/N '))
    while manual != 'y' and manual != 'Y' and manual != 'n' and manual != 'N':
        print('Limítese a usar Y o N')
        manual = str(input('¿Desea cargar las comidas de forma manual? Y/N '))
    if manual == 'Y' or manual == 'y':
        vector = funciones.crear_vector()
        funciones.cargar(vector)
    elif manual == 'N' or manual == 'n':
        vector = 12 * [None]
        funciones.auto_cargar(vector)
    while opcion != 7:
        mostrar_menu()
        opcion = int(input("Ingrese La opción deseada: "))
        print()

        if opcion == 1:
            funciones.mostrar_carta(vector)
            input("Presione enter para continuar\n")

        elif opcion == 2:
            print("El Precio promedio es $"+str(funciones.precio_promedio(vector)))
            input("Presione enter para continuar\n")

        elif opcion == 3:
            print("La comida con menor tiempo de cocción es", funciones.menor_tiempo_coccion(vector)[0], "y demora",
                  funciones.menor_tiempo_coccion(vector)[1], "minutos.")
            input("Presione enter para continuar\n")

        elif opcion == 4:
            clasif = input(
                "Elija la clasificación de su comida (0: Estandar / 1: Sin TACC / 2: Vegetariano / 3: Light): ")
            funciones.comida_tipo(clasif, vector)
            input("Presione enter para continuar\n")

        elif opcion == 5:
            nombre = input('Escriba el nombre del plato que desea buscar: ')
            funciones.buscar_y_sugerir(nombre, vector)
            input("Presione enter para continuar\n")

        elif opcion == 6:
            clasif = input(
                "Elija la clasificación de su comida (0: Estandar / 1: Sin TACC / 2: Vegetariano / 3: Light): ")
            funciones.menu_del_dia(vector, clasif)
            input("Presione enter para continuar\n")

        elif opcion == 7:
            print("¡Gracias por consultar nuestro menú!")
