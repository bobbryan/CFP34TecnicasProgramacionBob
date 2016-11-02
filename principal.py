import menu

opcionDelMenuElegida = menu.mostrarMenuInicial()

while (menu.validarOpcionesDelMenu(opcionDelMenuElegida) == False):
    opcionDelMenuElegida = menu.mostrarMenuInicial()

print("Bienvenido aljuego con la opcion",opcionDelMenuElegida)