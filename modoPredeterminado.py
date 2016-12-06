import nivelesPredeterminados
import menu
import coordenadas
import copy
import moduloDeUsuario

def jugar():
    print("Bienvenido al juego en modo PREDETERMINADO")
    tablero = copy.deepcopy(nivelesPredeterminados.getTablero(moduloDeUsuario.nivelActual))
    menu.mostrarTablero(tablero)

    #TODO hacer un bucle para ir jugando...


    print("---------------------------------------------------------")
    print("                 Ingrese una coordena")
    print("---------------------------------------------------------")
    print("         Ingresa la letra, seguido del  numero")
    print("---------------------------------------------------------")


    coordenadasDelUsuario = coordenadas.pedirCoordenadas()
    while not coordenadas.validarCoordenadas(coordenadasDelUsuario):
        print("")
        print("----------------------------------------------")
        print("    Ingrese una coordena CORRECTA   ")
        print("----------------------------------------------")
        coordenadasDelUsuario = coordenadas.pedirCoordenadas()

    traduccionDeCoordenada = coordenadas.transformacionDeCoordenadas(coordenadasDelUsuario)
    vecinos = coordenadas.buscaVecinos(traduccionDeCoordenada ,tablero)
    coordenadas.cambioDeCaracteres(traduccionDeCoordenada,tablero)
    coordenadas.cambioDeVecino(vecinos, tablero)
    menu.mostrarTablero(tablero)







