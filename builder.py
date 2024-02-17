class Veiculo:
    def __init__(self):
        self.modelo = ""
        self.motor = ""
        self.cor = ""

class VeiculoBuilder:
    def __init__(self):
        self.veiculo = Veiculo()
    def escolha_modelo(self, modelo):
        self.veiculo.modelo = modelo
    def escolha_motor(self, motor):
        self.veiculo.motor = motor
    def escolha_cor(self, cor):
        self.veiculo.cor = cor
    def encomendar_veiculo(self):
        return self.veiculo

class Diretor:
    def __init__(self, builder):
        self.builder = builder
    def construir_carro_luxo(self):
        self.builder.escolha_modelo("Fuscao")
        self.builder.escolha_motor("f-16")
        self.builder.escolha_cor("Preto")
    def construir_moto_esportiva(self):
        self.builder.escolha_modelo("XJ6")
        self.builder.escolha_motor("f-22")
        self.builder.escolha_cor("Verde")

builder = VeiculoBuilder()
diretor = Diretor(builder)
diretor.construir_carro_luxo()
carro_luxo = builder.encomendar_veiculo()
diretor.construir_moto_esportiva()
moto_esportiva = builder.encomendar_veiculo()


