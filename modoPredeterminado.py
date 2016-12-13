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


def terminar_juego():
    puntajeTotal = 0
    for clave in moduloDeUsuario.puntajePorNivel:
        puntajeTotal += moduloDeUsuario.puntajePorNivel[clave]

    print ("su puntaje TOTAL es:" + str (puntajeTotal))

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
        print("       Turnos restantes: "+str(turnos) )

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
        moduloDeUsuario.puntajePorNivel[moduloDeUsuario.nivelActual] += 500
        print("")
        print("Puntos por nivel: " + str(moduloDeUsuario.puntajePorNivel[moduloDeUsuario.nivelActual]))

        if moduloDeUsuario.nivelActual+1 < 6:
            moduloDeUsuario.nivelActual = moduloDeUsuario.nivelActual + 1
            jugar()
        else:
            terminar_juego()
    else:
        print("")
        print("Perdio, comienza nuevamente.")
        jugar()









