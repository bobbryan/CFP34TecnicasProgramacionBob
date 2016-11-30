import nivelesPredeterminados
import menu
import coordenadas

def jugar():
    print("Bienvenido al juego en modo PREDETERMINADO")
    menu.mostrarTablero(nivelesPredeterminados.primerNivel)
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
    print(traduccionDeCoordenada)

    #print(traduccionDeCoordenada[0])
    #print(traduccionDeCoordenada[1])

    vecinos = coordenadas.buscaVecinos(traduccionDeCoordenada ,nivelesPredeterminados.primerNivel)
    print(vecinos)


