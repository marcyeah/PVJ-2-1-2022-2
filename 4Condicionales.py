#NIVEL1
#EJERCICIO1
'''
a=int(input("ingrese el largo: "))
b=int(input("ingrese el ancho: "))
if a == b:
    print ("no es un cuadrado")
else:
    print ("es un cuadrado")
'''
#EJERCICIO2
'''
a=int(input("ingrese un número: "))
b=int(input("ingrese otro número: "))
c=input("ingrese un operador: ")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Operador no aceptado")
'''
#EJERCICIO3
'''
a=int(input("Ingrese los años de servicio del empleado: "))
b=float(input("Monto del salario: "))
if a>=3:
    bon=(b*5)/100
else:
     bon=0
print("la bonificacion es", bon")
'''
#EJERCICIO4
'''
p = int(input("Ingrese su puntaje: "))
if p<60:
    print("Su nota resultante es C")
elif p>=60 and p<80:
    print("Su nota resultante es B")
elif p>=80:
    print("Su nota  resultante es A")
'''

#NIVEL 2
#EJERCICIO2
'''
edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))
edad3 = int(input("Ingrese la edad de la tercera persona: "))
if edad1 < edad2:
    if edad1 < edad3:
        print("La edad del mas joven es",edad1)
    elif edad3 < edad2:
        if edad3 < edad1:
            print("La edad del mas joven es",edad3)
elif edad2 < edad1:
    if edad2 < edad3:
        print("La edad del mas joven es",edad2)
    elif edad3 < edad2:
        if edad3 < edad1:
            print("La edad del mas joven es",edad3)
'''
#EJERCICIO3
'''
l1 = float(input("Ingrese la longitud del lado a en cm: "))
l2 = float(input("Ingrese la longitud del lado b en cm: "))
l3 = float(input("Ingrese la longitud del lado c en cm: "))
if l1 == l2 and l2 == l3 and l1 == l3:
    print("Es un triángulo equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")
'''
#EJERCICIO4
'''
edad = int(input("Ingrese su edad: "))
if edad > 20 and edad <= 70:
    civ = input("Ingrese su estado civil ""C/S"": ")
    if civ == "C":
        print("Trabajará solo en zonas urbanas")
    elif civ == "S":
        if edad <= 50:
            print("Puede trabajar en cualquier lugar")
        elif edad > 50:
            print("Trabajará solo en áreas urbanas")
else:
    print("ERROR")
'''
#EJERCICIO5
'''
i = int(input("Ingrese el número de clases impartidas: "))
a = int(input("Ingrese el número de clases asistidas: "))
p = (a/i) * 100
if p <= 70:
    c = input("Ingrese 'S' si el alumno tiene causa medica y 'N' si no la tiene: ")
    if c == "S":
        print("El alumno es apto para presentarse al examen")
    else:
        print("El alumno no es apto para presentarse al examen")
elif p > 70:
    print("El alumno es apto para presentarse al examen")
'''
#EJERCICIO6
'''
lista=["Marzo", 10000, "Enero", 20000, "Febrero",21000]
b=int(input("Ingrese un valor: "))
if b>(lista[1]+lista[3]+lista[5]):
    boolean=True
else:
    boolean=False
'''
#EJERCICIO7
'''
lista=["Marzo", 10000, "Enero", 20000, "Febrero",21000]
b=int(input("Ingrese un valor: "))
if b>(lista[1]):
    boolean=True
elif b>(lista[3]):
    boolean=True
elif b>(lista[5]):
    boolean=True
else:
    boolean=False
'''
#EJERCICIO8
'''
a=int(input("Ingrese el año: "))
if a%4==0:
    print(a, "es un año bisiesto")
elif a%100==0:
    print(a, "no es un año bisiesto")
else:
    print(a, "no es un año bisiesto")
'''
#EJERCICIO9
# Con While
'''
n = ["Hugo", "Martin", "Lucas", "Mateo", "Leo", "Daniel", "Alejandro", "Pablo"]
nombre = input("Ingrese un nombre: ")
z = 0
while z < len(n):
    if n[z] == nombre:
        print(nombre, "se encuentra en la lista")
        z = len(n)+1
    else:
        z += 1
else:
    if z == len(n):
        print(nombre, "no se encuentra en la lista")
'''
# Con If
'''
n = ["Hugo", "Martin", "Lucas", "Mateo", "Leo", "Daniel", "Alejandro", "Pablo"]
nombre = input("Ingrese un nombre: ")
if nombre == n[0] or nombre == n[1] or nombre == n[2] or nombre == n[3] or nombre == n[4] or nombre == n[5] or nombre == n[6] or nombre == n[7]:
    print(nombre, "se encuentra en la lista")
else:
    print(nombre, "no se encuentra en la lista")
'''
#EJERCICIO10
'''
day = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
month = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
a = int(input("Ingrese un número entre 1 y 7: "))
b = int(input("Ingrese el número de día: "))
c = int(input("Ingrese un número entre 1 y 12: "))
print("Hoy es", day[a-1], b, "de", month[c-1])
'''