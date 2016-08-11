#coding:utf-8
import random

class restaurante():
    pass

# Creando la funcion para cargar los registros al vector
def init(plato, nom, clas, tip, tiem, prec ):
    plato.nombre = nom
    plato.clasificacion = clas
    plato.tipo = tip
    plato.tiempo = tiem
    plato.precio = prec

# La funcion que nos permite visualizar el vector de registros, de manera ordenada. evitando
# que al poner print() nos muestre la referencia en la memoria
def write(plato):
    print '- Tipo:', plato.tipo, ' '
    print '- Nombre:', plato.nombre, ' '
    print '- Clasificacion:', plato.clasificacion, ' '
    print '- Tiempo:', plato.tiempo, ' '
    print '- Precio:', plato.precio, ' '

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

       vector[x] = restaurante()
       init(vector[x],tipo,nombre,clasificacion, tiempo, precio )
    print()

# Carga del vector de manera aleatoria
def cargar_aleatorio():
    n = 3
    v = 3 * [None]
    for i in v:
        v[i] = random.randint(0,2)

def mostrar_menu():
    print("1)Consultar Carta")
    print("2)Calcular Precio Promedio")
    print("3)Buscar Comida Con Menor Tiempo De Cocción")
    print("4)Calcular y Mostrar La Cantidad De Comidas Por Tipo ")
    print("5)Buscar En La Carta Un Plato Principal")
    print("6)Mostrar El Menu Del Dia Completo")
    print("7)Salir")

opcion = 0

while opcion != 7:
    mostrar_menu()
    opcion = input("Ingrese La opción deseada: ")
    if opcion == 1:
        mostrar_carta()
    elif opcion == 2:
        precio_promedio()
    elif opcion == 3:
        menor_tiempo_coccion()
    elif opcion == 4:
        comida_tipo()
    elif opcion == 5:
        buscar_y_sugerir
    elif opcion == 6:
        menu_del_dia
    elif opcion== 7:
        print("Gracias por consultar nuestro menú")
        break
