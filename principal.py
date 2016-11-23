import menu
import modoPredeterminado

opcionDelMenuElegida = menu.mostrarMenuInicial()

while (not menu.opcionDelMenuValida(opcionDelMenuElegida)):
    opcionDelMenuElegida = menu.mostrarMenuInicial()

if opcionDelMenuElegida == "3":
    exit()
elif opcionDelMenuElegida == "2":
    modoPredeterminado.jugar()

else:
    # YA SE QUE ES 1 => llamar al modulo que juega aleatoriamente
    print("Bienvenido al juego con la opcion", opcionDelMenuElegida)










