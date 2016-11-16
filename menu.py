
def mostrarMenuInicial():

    print("-----------------------------------")
    print("BIENVENIDO AL JUEGO DE LAS LUCES !!")
    print("-----------------------------------")
    print("")
    print("A continuacion elija el su modo de juego ingresando 1 , 2 o 3 ")
    print("")
    print("1) Jugar en Modo aletorio")
    print("2) Jugar en Modo predeterminado")
    print("3) Salir")

    opcion = input("")
    return opcion


def validarOpcionesDelMenu(opcionElegida):

    opcionesDelJuego = ("1", "2","3")

    if opcionElegida in opcionesDelJuego:
        return True

    return False


