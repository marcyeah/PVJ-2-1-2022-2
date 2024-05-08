#EJERCICIO3
'''
a = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(a[:52])
'''
#EJERCICIO4
'''
a = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(a[53:])
'''
#EJERCICIO5
'''
a = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(a[5:11]+a[53:84])
'''
#EJERCICIO6
'''
a = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(a[49])
'''
#EJERCICIO7
'''
a = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
b = "se originan de una actitud de cariño por los demás"
print(a[:21]+"lindas"+a[27:43]+"la vida "+b[:])
'''
#EJERCICIO8
'''
a = ["Hola", "Amigos", "Hoy", True]
índice = int(input("ingrese la posición del término que desea eliminar en la lista ([""Hola"", ""Amigos"", ""Hoy"", True]): "))
a[índice-1:índice] = []
print(a)
'''
#EJERCICIO9
'''
a = ["Hola", "Amigos", "Hoy", True]
Word = [input("introduzca una palabra: ")]
a[0:0] =  Word
a[5:5] =  Word
print(a)
'''
#EJERCICIO10
'''
a = ["Hola", "Amigos", "Hoy", True]
a[0:1] = []
a[2:3] = []
print(a)
'''
#EJERCICIO11
'''
a = ["Hola", "Amigos", "Hoy", True]
a[3] = False
print(a)
'''
#EJERCICIO12
'''
a = ["Hola", "Amigos", "Hoy", True]
a[1] = input("Ingrese su nombre: ")
a[2] = input("Ingrese su apellido: ")
a[3] = int(input("Ingrese su edad: "))
print (a)
'''
#EJERCICIO13
'''
a = ["Hola", "Amigos", "Hoy", True]
name = [input("Ingrese su nombre: ")]
sec_name = [input ("Ingrese su apellido: ")]
age = [int(input("Ingrese su edad: "))]
a[0:0] = name
a[1:1] = sec_name
a[2:2] = age
print (a)
'''
#EJERCICIO14
'''a = ["Hola", "Amigos", "Hoy", True]
name = input("Ingrese su nombre: ")
sec_name = input ("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
a[0] = name
a[1] = sec_name
a[2] = age
print (a)
'''