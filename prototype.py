class Forma:
    def clone(self):
        return self.__class__()

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

if __name__ == "__main__":
    circulo_original = Circulo(raio=5)
    circulo_duplicado = circulo_original.clone()