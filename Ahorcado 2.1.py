import turtle
import random
def position_abc(a):
    for i in range(27):
        abc = "abcdefghijklmnñopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        if abc[i] == a or ABC[i] == a:
            return i
def mayus(a):
    ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    return(ABC[position_abc(a)])
def minus(a):
    abc = "abcdefghijklmnñopqrstuvwxyz"
    return(abc[position_abc(a)])
def tilde(a):
    áéí = "ábcdéfghíjklmnñópqrstúvwxyz"
    return(áéí[position_abc(a)])
def nt(a,b):
    c = 0
    for i in b:
        if a == i:
            c += 1
    return c
def position(a,b):
    for i in range(len(b)):
        if a == b[i] or mayus(a) == b[i] or minus(a) == b[i] or tilde(a) == b[i]:
            return i
def position_all(a,b):
    lista = []
    for i in range(len(b)):
        if minus(a) == b[i] or tilde(a) == b[i] or mayus(a) == b[i]:
            lista.append(i)
    return(lista)
def res(a,b):
    a = position_all(a,b)
    return(a[len(a)-1]-a[len(a)-2])
p = ["Avión", "Arándano", "Ademán", "Abejorro", "Aurora", "Compasión", "Complicidad", "Esperanza", "Estéreo", "Efímero", "Erudito", "Gentileza", "Inefable", "Inconmesurable", "Imprescindible", "Importante", "Melancolía", "Nostalgia", "Koala", "Ciudad", "Campo", "Posible", "Proceso", "Realidad", "Mentalidad", "Momento", "Murciélago", "Calidad"]
x = random.choice(p)
z = 35*len(x)
turtle.title("EL AHORCADO")
turtle.bgcolor("Black")
v = turtle.Screen()
t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t5 = turtle.Turtle()
c = (-20+19*len(x))-z+5
d = c + 6
t.penup()
t.goto(-200,-150)
t.pendown()
t.width(15)
t.hideturtle()
t2.hideturtle()
t2.penup()
t2.goto(c,240)
t3.hideturtle()
t3.penup()
t3.goto(0,0)
t3.hideturtle()
t3.penup()
t3.goto(0,0)
t5.hideturtle()
t5.penup()
t5.goto(0,0)
for i in range(len(x)+1):
    t2.pendown()
    t2.speed(0)
    t2.pencolor("#30BF78")
    t2.width(5)
    t2.forward(20)
    t2.penup()
    t2.goto(c,240)
    t2.pendown()
    t2.hideturtle()
    c += 35
t.pencolor("#FFFFFF")
t.forward(150)
t.penup()
t.goto(-125,-150)
t.pendown()
t.left(90)
t.forward(350)
t.right(90)
t.forward(200)
t.right(90)
t.forward(50)
t.right(90)
le = 0
fr = 0
lu = []
la = []
while le < 6:
    if len(la) == len(x):
        break
    l = turtle.textinput("AHORCADO", "Ingrese una letra: ")
    if len(l)>1 or position_abc(l) == None:
        t3.clear()
        t3 = turtle.Turtle()
        t3.hideturtle()
        t3.penup()
        t3.goto(0,-200)
        t3.pencolor("#FFFFFF")
        t3.write("El valor que usted ha ingresado no es válido", move = False, align = "center", font = ("Consolas", 15, "normal"))
        continue
    if l in lu:
        t3.clear()
        t3 = turtle.Turtle()
        t3.hideturtle()
        t3.penup()
        t3.goto(0,-200)
        t3.pencolor("#FFFFFF")
        t3.write("La letra" + " " + l + " " + "ya fue usada, ingrese otra letra", move = False, align = "center", font = ("Consolas", 15, "normal"))
        continue
    elif mayus(l) not in x and minus(l) not in x and tilde(l) not in x:
        t3.clear()
        t3 = turtle.Turtle()
        t3.hideturtle()
        t3.penup()
        t3.goto(0,-200)
        t3.pencolor("#FFFFFF")
        t3.write("La letra" + " " + l + " " + "no es parte de la palabra", move = False, align = "center", font = ("Consolas", 15, "normal"))
        le += 1
        lu.append(l)
    else:
        t3.clear()
        t3 = turtle.Turtle()
        t3.hideturtle()
        t3.penup()
        t3.goto(0,-200)
        t3.pencolor("#FFFFFF")
        t3.write("¡Acertaste! :D", move = False, align = "center", font = ("Consolas", 15, "normal"))
        n = position(l,x)
        m = position_all(l,x)
        w = nt(l,x)
        nm = 0
        if minus(l) == x[0] or mayus(l) == x[0]:
            p1 = d
            t4 = turtle.Turtle()
            t4.hideturtle()
            t4.penup()
            t4.goto(p1,245)
            t4.pencolor("#FFFFFF")
            t4.write(mayus(l), move = False, align = "left", font = ("Consolas", 15, "normal"))
            nm += 1
            la.append(l)
            if l in "aeiou" and tilde(l) in x:
                p1 = d+(35*m[1])
                t4 = turtle.Turtle()
                t4.hideturtle()
                t4.penup()
                t4.goto(p1,245)
                t4.pencolor("#FFFFFF")
                t4.write(tilde(l), move = False, align = "left", font = ("Consolas", 15, "normal"))
                nm += 1
                p1 += 35*m[1]
                lu.append(l)
                la.append(tilde(l))
            for h in m[nm:]:
                p1 = d+(35*h)
                t4 = turtle.Turtle()
                t4.hideturtle()
                t4.penup()
                t4.goto(p1,245)
                t4.pencolor("#FFFFFF")
                t4.write(l, move = False, align = "left", font = ("Consolas", 15, "normal"))
                nm += 1
                p1 += 35*h
                fr += 1
                n += res(l,x)
                la.append(l)
            lu.append(l)
            continue
        if l in "aeiou" and tilde(l) in x:
            p1 = d+(35*n)
            t4 = turtle.Turtle()
            t4.hideturtle()
            t4.penup()
            t4.goto(p1,245)
            t4.pencolor("#FFFFFF")
            t4.write(tilde(l), move = False, align = "left", font = ("Consolas", 15, "normal"))
            nm += 1
            p1 += 35*n
            la.append(l)
            lu.append(l)
            continue
        for o in m:
            p1 = d+(35*n)
            t4 = turtle.Turtle()
            t4.hideturtle()
            t4.penup()
            t4.goto(p1,245)
            t4.pencolor("#FFFFFF")
            t4.write(l, move = False, align = "left", font = ("Consolas", 15, "normal"))
            nm += 1
            p1 += 35*n
            fr += 1
            n += res(l,x)
            la.append(l)
        lu.append(l)
        continue
    if le == 1:
        t.color("#F2F5F4")
        t.begin_fill()
        t.speed(0)
        t.width(14)
        t.circle(35)
        t.end_fill()
        t.circle(35,180)
        t.width(15)
    t.speed(3)
    if le == 2:
        t.right(130)
        t.forward(65)
        t.penup()
        t.back(65)
        t.pendown()
    if le == 3:
        t.left(80)
        t.forward(65)
        t.penup()
        t.back(65)
        t.pendown()
    if le == 4:
        t.right(40)
        t.forward(60)
        t.forward(40)
    if le == 5:
        t.right(40)
        t.forward(65)
        t.penup()
        t.back(65)
        t.pendown()
    if le == 6:
        t.left(80)
        t.forward(65)
        t.penup()
        t.back(65)
        t.pendown()
    lu.append(l)
if le >= 6:
    t.pencolor("#F70202")
    t.speed(9)
    t.width(5)
    t.penup()
    t.goto(72,115)
    t.rt(85)
    t.fd(15)
    t.rt(100)
    t.pendown()
    t.fd(20)
    t.bk(10)
    t.rt(90)
    t.fd(10)
    t.bk(20)
    t.fd(10)
    t.rt(90)
    t.fd(10)
    t.lt(45)
    t.penup()
    t.fd(25)
    t.lt(45)
    t.pendown()
    t.forward(20)
    t.back(10)
    t.left(90)
    t.forward(10)
    t.back(20)
    t5.pencolor("#F70202")
    t5.write("HAS MUERTO, FIN DEL JUEGO", move = False, align = "center", font = ("Consolas", 20, "bold"))
    t3.clear()
    t3 = turtle.Turtle()
    t3.hideturtle()
    t3.penup()
    t3.goto(0,-200)
    t3.pencolor("#FFFFFF")
    t3.write("La letra" + " " + l + " " + "no es parte de la palabra,", move = False, align = "center", font = ("Consolas", 15, "normal"))
    t3.hideturtle()
    t3.penup()
    t3.goto(0,-225)
    t3.write("la palabra correcta era" + " " + "'" + x + "'", move = False, align = "center", font = ("Consolas", 15, "normal"))
    le += 1
    lu.append(l)
else:
    t3.clear()
    t5.pencolor("#05F545")
    t5.write("¡FELICIDADES, GANASTE EL JUEGO!", move = False, align = "center", font = ("Consolas", 20, "bold"))
    t3 = turtle.Turtle()
    t3.hideturtle()
    t3.penup()
    t3.goto(0,-200)
    t3.pencolor("#FFFFFF")
    t3.write("¡Encontraste la palabra!", move = False, align = "center", font = ("Consolas", 15, "normal"))
    t3.hideturtle()
    t3.penup()
    t3.goto(0,-225)
    t3.write("Número de intentos: " + str(len(la)+le), move = False, align = "center", font = ("Consolas", 15, "normal"))
turtle.mainloop()