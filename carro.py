import datetime

class Carro:
    def __init__(self, placa):
        self.placa = placa
        self.entrada = None
        self.saida = None
        self.local = None

    def estacionar(self, local: tuple[int], entrada: datetime.datetime, tempo: datetime.timedelta):
        self.local = local
        self.entrada = entrada
        self.saida = entrada + tempo

if __name__ == '__main__':
    entrada = datetime.datetime(2024, 10, 14, 16, 45)
    tempo = datetime.timedelta(hours=2)
    car = Carro("abc")
    car.estacionar((1,1), entrada, tempo)
    print(car.saida)