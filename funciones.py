class Restaurante():
    pass


# Creando la funcion para cargar los registros al vector
def init(plato, tip, nom, clas, tiem, prec):
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


# Se pasa a cargar los registros en el vector, tambien pregunta si desea ver el vector
def cargar(vector):
    n = len(vector)
    for x in range(0, n):
        tipo = input('Ingrese el tipo de plato (0: Entrada / 1: Principal / 2: Postre): ')
        nombre = input('Ingrese el nombre del plato: ')
        clasificacion = input('Ingrese la clasificacion (0: Estandar / 1: Sin TACC / 2: Vegetariano / 3: Light): ')
        tiempo = int(input('Ingrese el tiempo de cocción: '))
        precio = int(input('Ingrese el precio:  '))

        vector[x] = Restaurante()
        init(vector[x], tipo, nombre, clasificacion, tiempo, precio)
    print()


def mostrar_carta(vector):
    print('Valor del cubierto: $200 (Somos un restaurant prestigioso)')
    print()
    for i in vector:
        if i.tipo == 0:
            tipo = 'Entrada -'
        elif i.tipo == 1:
            tipo = 'Plato principal -'
        else:
            tipo = 'Postre -'
        print('Comida número', vector.index(i)+1)
        print(tipo, i.nombre, ' ')
        if i.clasificacion == 0:
            clasificacion = 'Estándar'
        elif i.clasificacion == 1:
            clasificacion = 'Sin TACC'
        elif i.clasificacion == 2:
            clasificacion = 'Vegetariano'
        else:
            clasificacion = 'Light'
        print('- Clasificacion:', clasificacion, ' ')
        print('- Tiempo de cocción:', i.tiempo, 'minutos ')
        print('- Precio: $'+str(i.precio), ' ')
        print()


def precio_promedio(vector):
    suma = 0
    for i in vector:
        suma += i.precio

    promedio = suma / len(vector)

    return promedio


def menor_tiempo_coccion(vector):
    valor = 999999
    nombre = 'NaN'
    for i in vector:
        if i.tiempo < valor:
            valor = i.tiempo
            nombre = i.nombre

    return nombre, valor


def comida_tipo(clasif, vector):
    x0 = 0
    x1 = 0
    x2 = 0
    y0 = 'NaN'
    y1 = 'NaN'
    y2 = 'NaN'
    if clasif == '0':
        z3 = 'estándar:'
    elif clasif == '1':
        z3 = 'sin TACC:'
    elif clasif == '2':
        z3 = 'vegetariano:'
    else:
        z3 = 'light:'
    for i in range(0, 12):
        if vector[i].clasificacion == int(clasif):
            if vector[i].tipo == 0:
                x0 += 1
                y0 = vector[i].nombre
            if vector[i].tipo == 1:
                x1 += 1
                y1 = vector[i].nombre
            if vector[i].tipo == 2:
                x2 += 1
                y2 = vector[i].nombre
    print('Tenemos', x0, 'entrada/s de tipo', z3, y0)
    print('Tenemos', x1, 'plato/s principale/s de tipo', z3, y1)
    print('Tenemos', x2, 'postre/s de tipo', z3, y2)
    # X = 5, Z = postres, Y = vegetarianos


def buscar_y_sugerir(nombre, vector):
    found = False
    vecont = 0
    arreglo = []
    for i in range(0, 12):
        if vector[i].nombre == nombre:
            found = True
            resultado = vector[i]
            print()
            print('Se ha encontrado un plato que coincide con su búsqueda')
            print()
    if found is True:
            if resultado.clasificacion == 0:
                clasi = 'de tipo estándar'
            elif resultado.clasificacion == 1:
                clasi = 'sin TACC'
            elif resultado.clasificacion == 2:
                clasi = 'vegetarianos'
            else:
                clasi = 'light'
            print('Los siguientes platos también son', clasi)
            print()
            for i in range(0, 12):
                if vector[i].clasificacion == resultado.clasificacion:
                    mostrar_vector(vector[i])
    elif found is False:
        print('Lo sentimos, no se han encontrado platos que coincidan con su búsqueda.')


def mostrar_vector(arg):
    print(arg.nombre, '- cuesta $'+str(arg.precio))


def menu_del_dia(vector, clasif):
    print()
    print('Menú del día: ')
    print()
    entrada = False
    princi = False
    postre = False
    precio = 0
    tiempo = 0
    for i in range(0, 12):
        if vector[i].clasificacion == int(clasif):
            if vector[i].tipo == 0 and entrada is False:
                mostrar_vector(vector[i])
                entrada = True
                precio += vector[i].precio
                tiempo += vector[i].tiempo
            if vector[i].tipo == 1 and princi is False:
                mostrar_vector(vector[i])
                princi = True
                precio += vector[i].precio
                tiempo += vector[i].tiempo
            if vector[i].tipo == 2 and postre is False:
                mostrar_vector(vector[i])
                postre = True
                precio += vector[i].precio
                tiempo += vector[i].tiempo
    print()
    print('El precio total del menú es de $'+str(precio))
    print('Podrá estar listo en aproximadamente', tiempo, 'minutos.')
    print()


def auto_cargar(vector):
    for x in range(0, 12):
        if 0 <= x <= 2:
            clasificacion = 0
        elif 3 <= x <= 5:
            clasificacion = 1
        elif 6 <= x <= 8:
            clasificacion = 2
        elif 9 <= x <= 12:
            clasificacion = 3
        if x == 0:
            tipo = 0
            nombre = 'Crêpes farcies de viande (Empanadas prestigiosas)'
        elif x == 1:
            tipo = 1
            nombre = 'Poulet pané avec pommes de terre (Mila prestigiosa de pollo)'
        elif x == 2:
            tipo = 2
            nombre = 'Yogourt avec des céréales (Yogurt prestigioso con cereales)'
        if x == 3:
            tipo = 0
            nombre = 'Ciboulette vinaigre (Cebollas prestigiosas)'
        elif x == 4:
            tipo = 1
            nombre = 'Saucisse de boeuf (Bife prestigioso de chorizo)'
        elif x == 5:
            tipo = 2
            nombre = 'Sorbet (Helado de agua prestigioso)'
        if x == 6:
            tipo = 0
            nombre = 'Salade (Ensalada prestigiosa)'
        elif x == 7:
            tipo = 1
            nombre = 'Soy Milan (Mila prestigiosa de soja)'
        elif x == 8:
            tipo = 2
            nombre = 'Riz au lait (Arroz prestigioso con leche)'
        if x == 9:
            tipo = 0
            nombre = 'Pain avec de la mayonnaise (Pan prestigioso con mayonesa light)'
        elif x == 10:
            tipo = 1
            nombre = 'Hamburgers (Hamburguesas prestigiosas light)'
        elif x == 11:
            tipo = 2
            nombre = 'Dessertito être (Postrecito prestigioso "Ser")'
        tiempo = 60 - (x + 1) * 4
        precio = 250 + (x + 1) * 4 + 0.99
        vector[x] = Restaurante()
        init(vector[x], tipo, nombre, clasificacion, tiempo, precio)

    print()
