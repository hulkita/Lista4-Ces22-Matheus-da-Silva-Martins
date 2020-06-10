class Veiculo:
    def __init__(self, tipo_motorizacao):
        self.tipo_motorizacao = tipo_motorizacao


    def motor_type(self):
        return self.tipo_motorizacao
    def caracteristicas(self):
        pass

class Caminhao(Veiculo):
    def caracteristicas(self):
        print("Veiculo de carga, caminhao")
        return

class Automovel(Veiculo):
    def caracteristicas(self):
        print("Veiculo de uso pessoal, carro")
class Moto(Veiculo):
    def caracteristicas(self):
        print("Veiculo de alta mobilidade, moto")
        return

class Fabrica:
    def identificar(self, tipo_veiculo):
        if tipo_veiculo == 'caminhao':
            return Caminhao('caminhao')
        elif tipo_veiculo == 'automovel':
            return Automovel('automovel')
        elif tipo_veiculo == 'moto':
            return Moto('moto')

fabrica = Fabrica()
carro = fabrica.identificar('automovel')
carro.caracteristicas()

caminhao1 = fabrica.identificar('caminhao')
caminhao1.caracteristicas()

moto1 = fabrica.identificar('moto')
moto1.caracteristicas()

