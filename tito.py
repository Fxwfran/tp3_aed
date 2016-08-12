import random
import funciones


class Restaurante():
    pass


# Creando la funcion para cargar los registros al vector
def init(plato, nom, clas, tip, tiem, prec):
    plato.nombre = nom
    plato.clasificacion = clas
    plato.tipo = tip
    plato.tiempo = tiem
    plato.precio = prec





# Pedimos el largo del vector y creamos uno de n Nones
def crear_vector():
    n = int(input('Ingrese la cantidad de platos que desea cargar: '))
    vector = n * [None]

    return vector


# Se pasa a cargar los registros en el vector, tambien pregunta si desea ver el vector
def cargar(vector):
    n = len(vector)
    for x in range(n):
        print()
        tipo = input('Ingrese el tipo de plato: ')
        nombre = input('Ingrese el nombre del plato: ')
        clasificacion = input('Ingrese la clasificacion: ')
        tiempo = int(input('Ingrese el tiempo de cocción: '))
        precio = int(input('Ingrese el precio:  '))

        vector[x] = Restaurante()
        init(vector[x], tipo, nombre, clasificacion, tiempo, precio)

    print()


# Carga del vector de manera aleatoria
def cargar_aleatorio():
    n = 3
    v = 3 * [None]
    for i in v:
        v[i] = random.randint(0, 2)

def mostrar_carta(vector):
    for i in vector:
        print ('- Tipo:', i.tipo, ' ')
        print ('- Nombre:', i.nombre, ' ')
        print ('- Clasificacion:', i.clasificacion, ' ')
        print ('- Tiempo:', i.tiempo, ' ')
        print ('- Precio:', i.precio, ' ')
        print("\n")

def precio_promedio(vector):
    suma = 0
    for i in vector:
        suma+= i.precio

    promedio = suma / len(vector)

    return promedio

def menor_tiempo_coccion(vector):
    valor = 999999

    for i in vector:
        if i.tiempo < valor:
            valor = i.tiempo

    return valor




def mostrar_menu():
    print("1)Consultar carta: ")
    print("2)Calcular precio promedio: ")
    print("3)Buscar comida con menor tiempo de cocción: ")
    print("4)Calcular y mostrar la cantidad de comidas por tipo: ")
    print("5)Buscar en la carta un plato principal: ")
    print("6)Mostrar el menu del día completo: ")
    print("7)Salir")

opcion = 0

if __name__ == "__main__":
    manual = input('¿Desea cargar las comidas de forma manual? Y/N')
    if manual == 'Y' or manual == 'y':
        vector = crear_vector()
        cargar(vector)
        while opcion != 7:
            mostrar_menu()
            opcion = int(input("Ingrese La opción deseada: "))
            
            if opcion == 1:
                mostrar_carta(vector)
                input("precione enter para continuar\n")
            
            elif opcion == 2:
                print("El Precio promedio es $",precio_promedio(vector))
                input("precione enter para continuar\n")
            
            elif opcion == 3:
                print("El menor tiempo de cocción es",menor_tiempo_coccion(vector))
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
