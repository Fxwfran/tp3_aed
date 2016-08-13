import random
comidas = "milanesas", "asado", "hamburguesas", "tortillas","alfajor", "flan", "helado", "frutillas con crema"\
    ,"vitel tone", "Tabla de fiambres", "empanadas", "piza"
tipos = "Entrada", "Principal", "Postre"
clasificaciones = "Sin TACC", "estandar", "Vegetariano", "Light"
precios = 100, 50, 80, 60, 90
tiempos = 10, 50, 60, 20, 30

class Restaurante():
    pass


# Creando la funcion para cargar los registros al vector
def init(plato,tip, nom, clas, tiem, prec):
    plato.tipo = tip
    plato.nombre = nom
    plato.clasificacion = clas
    plato.tiempo = tiem
    plato.precio = prec



# Pedimos el largo del vector y creamos uno de n Nones
def crear_vector():
    n = int(input('Ingrese la cantidad de platos que desea cargar: '))
    vector = n * [None]

    return vector
# Crea el vector
def crear():
    vector = 5 * [None]
    return vector


# Se pasa a cargar los registros en el vector
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




# Carga del vector de manera aleatoria
def cargar_aleatorio(vector):
    n = len(vector)
    for x in range(n):
        tipo = random.choice(tipos)
        nombre = random.choice (comidas)
        clasificacion = random. choice (clasificaciones)
        tiempo = random.choice(tiempos)
        precio = random.choice(precios)

        vector[x] = Restaurante()
        init(vector[x], tipo, nombre, clasificacion, tiempo, precio)



# Las 3 Funciones ya listas del menu
def mostrar_carta(vector):
    for i in vector:
        print ('- Tipo:', i.tipo, ' ')
        print ('- Nombre:', i.nombre, ' ')
        print ('- Clasificacion:', i.clasificacion, ' ')
        print ('- Tiempo:', i.tiempo,'Min ')
        print ('- Precio:$',i.precio, ' ')
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
            comida = i.nombre
    print("El plato con menor tiempo de cocción es  tiempo de cocción es",comida, "con tiempo", valor)



#Menu
def mostrar_menu():
    print("1)Consultar carta: ")
    print("2)Calcular precio promedio: ")
    print("3)Buscar comida con menor tiempo de cocción: ")
    print("4)Calcular y mostrar la cantidad de comidas por tipo: ")
    print("5)Buscar en la carta un plato principal: ")
    print("6)Mostrar el menu del día completo: ")
    print("7)Salir")



