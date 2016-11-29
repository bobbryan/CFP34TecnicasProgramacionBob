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
    columna = diccionarioLetras[coordenada[0]]
    fila = int(coordenada[1]) - 1

    return columna,fila