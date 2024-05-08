import random
import time

def nint(val):
    try:
        return int(val)
    except:
        print(f"Error: el valor ingresado '{val}' no es un número entero")
        return -1    
def tablero(tab, mode):
    if mode == 0:
        cont = 1
        col = ['1', '2', '3']
        print("="*48 + "\n[f]    Tablero")
        for row in tab:
            print(' ' + str(cont) + " [", " ][ ".join(row),"]")
            cont += 1
        print('     ' + '    '.join(col) + '  [c]')
    if mode == 1:
        print("="*48 + "\n    Tablero")
        for row in tab:
            print("[", " ][ ".join(row),"]")
def victoria(tab, p):
    for i in tab:
        if all(pos == p for pos in i):
            return True
    for j in range(3):
        if all(tab[i][j] == p for i in range(3)):
            return True
    if all(tab[k][k] == p for k in range(3)) or all(tab[k][2-k] == p for k in range(3)):
        return True
    return False
def game_mode():
    while True:
        q = nint(input("Elige el modo de juego pvp(1)/pc(2): "))
        if (q > 2 or q < 1) and q != -1:
            print("Error: el valor ingresado excede los parámetros dados, vuelva a intentar")
            continue
        elif q == -1:
            continue 
        else: 
            return q
        
matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
a = random.randint(0, 1)
x = 0
p = 0
print("TicTacToe - Original Version")
q = game_mode()
lock = 0

while q == 1:
    e = 0
    b = 'X' if x % 2 == 0 else 'O'
    if x == 0:
        print(f"Empieza el jugador '{b}'")
    elif x > 0:
        print(f"Turno del jugador '{b}'")
    tablero(matriz, 0)
    while True:
        while True:
            f = nint(input(f"Jugador {b} ingrese la fila [f]: ")) - 1
            if f == -2:
                continue
            elif f < 0 or f > 2:
                print("Error: el valor ingresado excede los parámetros dados")
                continue
            break
        while True:
            c = nint(input(f"Jugador {b} ingrese la columna [c]: ")) - 1
            if c == -2:
                continue
            elif c < 0 or c > 2:
                print("Error: el valor ingresado excede los parámetros dados")
                continue
            break
        if matriz[f][c] != " ":
            print("Error: este sitio está ocupado")
            continue
        else:
            matriz[f][c:c+1] = b
            x += 1
            break
    print()
    if victoria(matriz, b):
            tablero(matriz, 1)
            print(f"¡El jugador {b} ha ganado!")
            break
    elif x == 9:
        tablero(matriz, 1)
        print("Empate, no hay ganadores")
        break

while q == 2:
    e = 0
    if x == 0:
        b = input("Elige 'X'/'O': ")
    if x % 2 == 1:
        if b == 'O':
            b = 'X'
        else:
            b = 'O'
        print(f"Turno de la pc '{b}'")
    elif x % 2 == 0:
        if b == 'O' and x != 0:
            b = 'X'
        else:
            b = 'O'
        print(f"Turno del jugador '{b}'")
        tablero(matriz, 0)
    if x % 2 == 1:
        time.sleep(2)
        cont = 0
        while lock == 0:
            if cont == 4:
                lock = 1
            f = random.choice([0,2])
            c = random.choice([0,2])
            if f >= 0 and f < 3 and c >= 0 and c < 3 and matriz[f][c] == " ":
                matriz[f][c:c+1] = b
                break
            cont += 1
        while lock == 1:
            f = random.randint(0,2)
            c = random.randint(0,2)
            if f >= 0 and f < 3 and c >= 0 and c < 3 and matriz[f][c] == " ":
                matriz[f][c:c+1] = b
                break
        x += 1
        tablero(matriz, 1)
        time.sleep(3)
    while x % 2 == 0:
        while True:
            f = nint(input(f"Jugador {b} ingrese la fila [f]: ")) - 1
            if f == -2:
                continue
            elif f < 0 or f > 2:
                print("Error: el valor ingresado excede los parámetros dados")
                continue
            break
        while True:
            c = nint(input(f"Jugador {b} ingrese la columna [c]: ")) - 1
            if c == -2:
                continue
            elif c < 0 or c > 2:
                print("Error: el valor ingresado excede los parámetros dados")
                continue
            break
        if matriz[f][c] != " ":
            print("Error: este sitio está ocupado")
            continue
        else:
            matriz[f][c:c+1] = b
            x += 1
            break
    print()
    if victoria(matriz, b):
            tablero(matriz, 1)
            print(f"¡El jugador {b} ha ganado!")
            break
    elif x == 9:
        tablero(matriz, 1)
        print("Empate, no hay ganadores")
        break

print("\n" + "[made by marcyeah]" + "\n")