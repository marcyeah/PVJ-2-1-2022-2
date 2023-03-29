class dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + "," + " " + str(self.y) + ")"
class rec:
    def __init__(self, ancho, altura, puntoIni):
        self.altura = altura
        self.ancho = ancho
        self.puntoIni = puntoIni
    def calcularArea(self):
        area = self.altura * self.ancho
        return area
    def calcularPerimetro(self):
        perimetro = 2* (self.altura +self.ancho)
        return perimetro
    def calcularEsquina(self):
        esquina = dot(self.puntoIni.x + self.altura, self.puntoIni.y + self.ancho)
        return esquina
    def __add__(self, ot_rec):
        return 
def main():
    p1 = dot(10, 14)
    r = rec(4, 2, p1)
    a1 = r.calcularEsquina()
    print(a1)
main()
        
        
