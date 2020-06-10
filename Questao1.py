class Veiculo:
    def __init__(self, tipo_motorizacao, forca):
        self.tipo_motorizacao = tipo_motorizacao
        self.forca_do_motor = forca

    def motor_type(self):
        return self.tipo_motorizacao
    def forca_number(self):
        return self.forca_do_motor
    def caracteristicas(self):
        pass

class Caminhao(Veiculo):
    def caracteristicas(self):
        print("Veiculo de carga")
        return

class Automovel(Veiculo):
    def caracteristicas(self):
        print("Veiculo de uso pessoal")
class Moto(Veiculo):
    def caracteristicas(self):
        print("Veiculo de alta mobilidade")
