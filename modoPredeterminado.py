import nivelesPredeterminados
import menu
import coordenadas

def jugar():
    print("Bienvenido al juego en modo PREDETERMINADO")
    menu.mostrarTablero(nivelesPredeterminados.primerNivel)
    print("-----------------------------------")
    print("       Ingrese una coordena")
    print("-----------------------------------")
    print("  Ingresa la FILA, seguido de la COLUMNA")
    print("-----------------------------------")


    coordenadasDelUsuario = coordenadas.pedirCoordenadas()
    while not coordenadas.validarCoordenadas(coordenadasDelUsuario):
        print("-----------------------------------")
        print("    Ingrese una coordena CORRECTA   ")
        print("-----------------------------------")
        coordenadasDelUsuario = coordenadas.pedirCoordenadas()




