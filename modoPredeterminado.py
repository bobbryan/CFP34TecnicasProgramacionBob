import nivelesPredeterminados
import menu
import coordenadas

def jugar():
    print("Bienvenido al juego en modo PREDETERMINADO")
    menu.mostrarTablero(nivelesPredeterminados.primerNivel)
    print("---------------------------------------------------------")
    print("                 Ingrese una coordena")
    print("---------------------------------------------------------")
    print("  Ingresa la FILA (letra), seguido de la COLUMNA (numero)")
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

    print(traduccionDeCoordenada[0])
    print(traduccionDeCoordenada[1])
