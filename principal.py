import menu

opcionDelMenuElegida = menu.mostrarMenuInicial()

while (menu.validarOpcionesDelMenu(opcionDelMenuElegida) == False):
    opcionDelMenuElegida = menu.mostrarMenuInicial()

if opcionDelMenuElegida == "3":
    exit()
elif opcionDelMenuElegida == "2":
    # Si es 2 => llamar al modulo que juega predeterminado
    print("Bienvenido al juego con la opcion", opcionDelMenuElegida)
else:
    # YA SE QUE ES 1 => llamar al modulo que juega aleatoriamente
    print("Bienvenido al juego con la opcion", opcionDelMenuElegida)









