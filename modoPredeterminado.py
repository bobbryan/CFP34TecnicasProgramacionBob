import nivelesPredeterminados
import menu
import coordenadas
import copy
import moduloDeUsuario


def estaJugoGanadoPara(tablero):

    for fila in tablero:
        for elemento in fila:
            if elemento != ".":
                return False

    return True

def condicionParaSeguirJugando(turnos,tablero):

    hayTurnosDisponibles = turnos > 0
    juegoGanado = estaJugoGanadoPara(tablero)

    return hayTurnosDisponibles and not juegoGanado



def jugar():
    print("")
    print("Bienvenido al juego en modo PREDETERMINADO Nivel " + str(moduloDeUsuario.nivelActual))
    print("")

    tablero = copy.deepcopy(nivelesPredeterminados.getTablero(moduloDeUsuario.nivelActual))
    menu.mostrarTablero(tablero)
    print("")

    turnos = 15
    while condicionParaSeguirJugando(turnos,tablero):
        print("---------------------------------------------------------")
        print("                 Ingrese una coordena")
        print("---------------------------------------------------------")
        print("         Ingresa la letra, seguido del  numero")
        print("---------------------------------------------------------")
        print("                  Turnos restantes: "+str(turnos))
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
        turnos = turnos -1

    if estaJugoGanadoPara(tablero):
        moduloDeUsuario.nivelActual = moduloDeUsuario.nivelActual +1
    else:
        print("")
        print("Perdio, comienza nuevamente.")

    jugar()














