#NIVEL1
#EJERCICIO1
#n = int(input("Ingrese un número: "))
#x = 1
#z = 0
#while z < 100:
#    print(n*x)
#    x += 1
#    z += 1
#EJERCICIO2
#a = []
#z = 0
#y = 0
#s = 0
#while z <= 9:
#    if z == 0:
#        n = [int(input("Ingrese un valor: "))]
#        a[z:z] = n
#        z += 1
#    else:
#        n = [int(input("Ingrese otro valor: "))]
#        a[z:z] = n
#        z += 1
#while y <= 9:
#    s = s + a[y]
#    y += 1
#print("El promedio de los números que usted ingresó es", s/10)
#EJERCICIO4
#x=0
#y=1
#print(x)
#print(y)
#while x+y<=100:
#    aux=x+y
#    print(aux)
#    x=y
#    y=aux
#EJERCICIO11
#lista = []
#z = 0
#y = 0
#x = 0
#while z < len(lista)+1:
#    if len(lista) < 1:
#        a = [input("Introduce una palabra: ")]
#        lista[z:z] = a
#        z += 1
#    else:
#        a = [input("Introduce otra palabra, añade un punto para finalizar la lista: ")]
#        lista[z:z] = a
#        w = lista[z]
#        z += 1
#        if w[len(w)-1] == ".":
#            lista[z-1] = w[:len(w)-1]
#            z = len(lista)+1
#while x < len(lista):
#    i = len(lista[y])
#    o = len(lista[y+1])
#    if i >= o:
#        lista[y:y+1] = []
#        x += 1
#    elif i < o:
#        lista[y:y+1] = []
#        x += 1
#l = (len(lista[y]))
#EJERCICIO13


#NIVEL2
#EJERCICIO5
#p = input("Ingrese un cáracter: ")
#h = int(input("Ingrese la altura de la pirámide: "))
#z = 0
#c = 1
#s = 1
#while z<h:
#    print(" "*(h-c)+p*s)
#    z+=1
#    c+=1
#    s+=2
#EJERCICIO6
#i = 4
#j = 1
#simbolo1 = input("Ingrese primer  símbolo:")
#simbolo2 = input("Ingrese segundo  símbolo:")
#while i >= 0:
#  print(" " * i + simbolo1 * j)
#  j += 2
#  i -= 1
#i = 1
#j = 7
#while j > 0:
#  print(" " * i + simbolo2 * j)
#  i += 1
#  j -= 2
#EXTRA
#lista = []
#z = 0
#y = 0
#x = 0
#while z < len(lista)+1:
#    if len(lista) < 1:
#        a = [input("Introduce una palabra: ")]
#        lista[z:z] = a
#        z += 1
#    else:
#        a = [input("Introduce otra palabra, añade un punto para finalizar la lista: ")]
#        lista[z:z] = a
#        w = lista[z]
#        z += 1
#        if w[len(w)-1] == ".":
#            lista[z-1] = w[:len(w)-1]
#            z = len(lista)+1
#while x < len(lista)-1:
#    lista[len(lista):len(lista)] = [lista[y]]
#    x += 1
#    if lista[y] in lista:
#        lista[y:y+1] = []
#lista[1:1] = [lista[len(lista)-1]]
#lista[len(lista)-1:len(lista)] = []
#print(lista)
