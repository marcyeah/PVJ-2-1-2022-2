from random import randint

def nint(val):
    try:
        return int(val)
    except:
        print("Error: el valor ingresado no es de clase " + '"' + "int" + '"')
        return -1

lista = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
a = randint(0, 1)
x = 0
p = 0
q = 1
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
    print("="*48 + "\n" + "Tablero")
    while p<3:
        print("|", lista[p][0], "|", lista[p][1], "|", lista[p][2], "|")
        p += 1
    p = 0
    while True:
        f = nint(input("Jugador '" + b + "' ingrese la fila (1-3): ")) - 1
        if f == -2:
            continue
        elif f < 0 or f > 2:
            print("Error: el valor que usted ha ingresado excede los parámetros dados")
            continue
        c = nint(input("Jugador" + " " + b + ", ingrese la columna (1-3): ")) - 1
        if c == -2:
            continue
        if c < 0 or c > 2:
            print("Error: el valor que usted ha ingresado excede los parámetros del juego, por favor respete los parámetros señalados")
            continue
        elif f >= 0 and f < 3 and c >= 0 and c < 3 and lista[f][c] == " ":
            lista[f][c:c+1] = b
            break
        elif b != " ":
            print("Error: este sitio ya está ocupado, por favor elija otra posición")
            continue
    x += 1
    for i in lista:
        d1 = [lista[0][0], lista[1][1], lista[2][2]]
        d2 = [lista[0][2], lista[1][1], lista[2][0]]
        if i == ["X", "X", "X"] or i == ["O", "O", "O"] or d1 == ["X", "X", "X"] or d1 == ["O", "O", "O"] or d2 == ["X", "X", "X"] or d2 == ["O", "O", "O"]:
            print("="*48 + "\n" + "Tablero")
            while p<3:
                print("|", lista[p][0], "|", lista[p][1], "|", lista[p][2], "|")
                p += 1
            print("¡El jugador '" + b + "' es el ganador de esta partida!")
            q = 0
            break
        else:
            break
    while e<3:
        y = [lista[0][e], lista[1][e], lista[2][e]]
        if y == ["X", "X", "X"] or y == ["O", "O", "O"]:
            print("="*48 + "\n" + "Tablero")
            while p<3:
                print("|", lista[p][0], "|", lista[p][1], "|", lista[p][2], "|")
                p += 1
            print("¡El jugador '" + b + "' es el ganador de esta partida!")
            q = 0
        e += 1
    if x == 9:
        print("="*48 + "\n" + "Tablero")
        while p<3:
            print("|", lista[p][0], "|", lista[p][1], "|", lista[p][2], "|")
            p += 1
        print("Empate, no hay ganadores")
        break