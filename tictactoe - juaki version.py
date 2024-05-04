from random import randint

def nint(val):
    try:
        return int(val)
    except:
        print("Error: el valor ingresado '" + val + "' no es de clase " + '"' + "int" + '"')
        return -1
def val(cord, c):       
    try:
        return nint(cord.split(',')[c]) - 1
    except:
        print ("Error: uno de los valores ingresados no respeta los parámetros dados")
        return -1

matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
a = randint(0, 1)
x = 0
p = 0
q = 1
print("TicTacToe - Juaki's version")
while q == 1:
    e = 0
    if a == 0:
        b = "X"
        a += 1
    elif a == 1:
        b = "O"
        a -= 1
    if x == 0:
        print ("Empieza el jugador '" + b + "'")
    elif x > 0:
        print("Turno del jugador '" + b + "'")
    print("="*48 + "\n" + "[f]" + '    ' "Tablero")
    while p<3:
        print(' ' + str(p+1) + ' ' + "[", matriz[p][0], "][", matriz[p][1], "][", matriz[p][2], "]")
        p += 1
    p = 0
    print('     ' + '1' + '    ' + '2' + '    ' + '3' + '  ' + '[c]')
    while True:
        cord = input("Jugador '" + b + "' ingrese las coordenadas en el formato (f,c): ")
        f = val(cord, 0)
        if f == -1 or f == -2:
            continue
        c = val(cord, 1)
        if c == -1 or c == -2:
            continue
        if f < 0 or f > 2 or c < 0 or c > 2:
            print("Error: los valores ingresados exceden los parámetros dados")
            continue
        elif f >= 0 and f < 3 and c >= 0 and c < 3 and matriz[f][c] == " ":
            matriz[f][c:c+1] = b
            break
        elif b != " ":
            print("Error: este sitio ya está ocupado, por favor elija otra posición")
            continue
    print()
    x += 1
    for i in matriz:
        d1 = [matriz[0][0], matriz[1][1], matriz[2][2]]
        d2 = [matriz[0][2], matriz[1][1], matriz[2][0]]
        if i == ["X", "X", "X"] or i == ["O", "O", "O"] or d1 == ["X", "X", "X"] or d1 == ["O", "O", "O"] or d2 == ["X", "X", "X"] or d2 == ["O", "O", "O"]:
            print("="*48 + "\n" + "    Tablero")
            while p<3:
                print("[", matriz[p][0], "][", matriz[p][1], "][", matriz[p][2], "]")
                p += 1
            print("¡El jugador '" + b + "' es el ganador de esta partida!")
            q = 0
            break
    while e<3:
        y = [matriz[0][e], matriz[1][e], matriz[2][e]]
        if y == ["X", "X", "X"] or y == ["O", "O", "O"]:
            print("="*48 + "\n" + "    Tablero")
            while p<3:
                print("[", matriz[p][0], "][", matriz[p][1], "][", matriz[p][2], "]")
                p += 1
            print("¡El jugador '" + b + "' es el ganador de esta partida!")
            q = 0
        e += 1
    if x == 9:
        print("="*48 + "\n" + "    Tablero")
        while p<3:
            print("[", matriz[p][0], "][", matriz[p][1], "][", matriz[p][2], "]")
            p += 1
        print("Empate, no hay ganadores")
        break
print("\n" + "[made by marcyeah]" + "\n")