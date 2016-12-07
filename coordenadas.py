def pedirCoordenadas():
    coordenada=input("")
    return (coordenada)

def validarCoordenadas(coordenada):
    coordenadasValidas = ("a1","a2","a3","a4","a5","b1","b2","b3","b4","b5","c1","c2","c3","c4","c5","d1","d2","d3","d4","d5","e1","e2","e3","e4","e5")
    if coordenada in coordenadasValidas :
        return True
    return False

def transformacionDeCoordenadas(coordenada):
    diccionarioLetras = {'a':0,'b':1,'c':2,'d':3,'e':4}
    fila  = diccionarioLetras[coordenada[0]]
    columna = int(coordenada[1]) - 1

    return columna,fila

def vecinoValido(coordenada,tablero):
    x = coordenada[0]
    y = coordenada[1]
    limiteInferior =  -1
    limiteSuperior =  5
    if limiteInferior < x < limiteSuperior and limiteInferior < y < limiteSuperior:
        return True



    # TODO para saber si una coordenada es valida tengo que chequear:
    # LIMITE_INFERIOR < X < LIMITE SUPERIOR
    # LIMITE_INFERIOR < Y < LIMITE SUPERIOR
    # Si las 4 cosas se cumples => True, sino False


def buscaVecinos(coordenada,tablero):

    vecinos = []

    coordenaPrincipal = coordenada
    verticalSuperior = coordenaPrincipal[0] , int(coordenaPrincipal[1]) - 1
    verticalInferior = coordenaPrincipal[0] , int(coordenaPrincipal[1]) + 1
    horizontalDerecho = int(coordenaPrincipal[0]) + 1 , coordenaPrincipal[1]
    horizontalIzquierdo = int(coordenaPrincipal[0]) - 1 , coordenaPrincipal[1]


    if vecinoValido(verticalSuperior,tablero):
        vecinos.append(verticalSuperior)

    if vecinoValido(verticalInferior,tablero):
        vecinos.append(verticalInferior)

    if vecinoValido(horizontalDerecho,tablero):
        vecinos.append(horizontalDerecho)

    if vecinoValido(horizontalIzquierdo,tablero):
        vecinos.append(horizontalIzquierdo)

    return vecinos


caracteres = {"0": ".", ".": "0"}

def cambioDeCaracteres(coordenada,tablero):
    fila = coordenada[0]
    columna = coordenada[1]

    caracterCambiado = caracteres[tablero[fila][columna]]

    tablero[fila][columna] = caracterCambiado


def cambioDeVecino (vecinos,tablero):

    for coordenadas in vecinos:
        cambioDeCaracteres(coordenadas,tablero)

