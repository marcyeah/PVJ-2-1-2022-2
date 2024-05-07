from random import randint

def nint(val):
    try:
        return int(val)
    except:
        print("Error: el valor ingresado no es de clase " + '"' + "int" + '"')
        return -1

matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
a = randint(0, 1)
x = 0
p = 0
q = 1
print("TicTacToe - Original Version")
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
    print("="*38 + "\n" + "[f]" + '   ' "Tablero")
    while p<3:
        print(' ' + str(p+1) + ' ' + "[", matriz[p][0], "|", matriz[p][1], "|", matriz[p][2], "]")
        p += 1
    p = 0
    print('     ' + '1' + '   ' + '2' + '   ' + '3' + '  ' + '[c]')
    while True:
        while True:
            f = nint(input("Jugador '" + b + "' ingrese la fila (1-3): ")) - 1
            if f == -2:
                continue
            elif f < 0 or f > 2:
                print("Error: el valor que usted ha ingresado excede los parámetros dados")
                continue
            break
        while True:
            c = nint(input("Jugador" + " " + b + ", ingrese la columna (1-3): ")) - 1
            if c == -2:
                continue
            elif c < 0 or c > 2:
                print("Error: el valor que usted ha ingresado excede los parámetros dados")
                continue
            break
        if f >= 0 and f < 3 and c >= 0 and c < 3 and matriz[f][c] == " ":
            matriz[f][c:c+1] = b
            x += 1
            break
        elif b != " ":
            print("Error: este sitio ya está ocupado, por favor elija otra posición")
            continue
    print()
    for i in matriz:
        d1 = [matriz[0][0], matriz[1][1], matriz[2][2]]
        d2 = [matriz[0][2], matriz[1][1], matriz[2][0]]
        if i == [b, b, b] or d1 == [b, b, b] or d2 == [b, b, b]:
            print("="*38 + "\n" + "Tablero")
            while p<3:
                print("[", matriz[p][0], "|", matriz[p][1], "|", matriz[p][2], "]")
                p += 1
            print("¡El jugador '" + b + "' es el ganador de esta partida!")
            q = 0
            break
    while e<3:
        y = [matriz[0][e], matriz[1][e], matriz[2][e]]
        if y == [b, b, b]:
            print("="*38 + "\n" + "Tablero")
            while p<3:
                print("[", matriz[p][0], "|", matriz[p][1], "|", matriz[p][2], "]")
                p += 1
            print("¡El jugador '" + b + "' es el ganador de esta partida!")
            q = 0
        e += 1
    if x == 9:
        print("="*38 + "\n" + "Tablero")
        while p<3:
            print("[", matriz[p][0], "|", matriz[p][1], "|", matriz[p][2], "]")
            p += 1
        print("Empate, no hay ganadores")
        break
print("\n" + "[made by marcyeah]" + "\n")
