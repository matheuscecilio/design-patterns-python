from datetime import date

class Contrato():
    def __init__(self, data, cliente, tipo = 'NOVO'):
        self.__tipo = tipo
        self.__data = data
        self.__cliente = cliente

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def avanca(self):
        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO': 
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self):
        contrato = Contrato(
            data = self.__data,
            cliente = self.__cliente,
            tipo = self.__tipo
        )

        return Estado(contrato)

    def restaura_estado(self, estado):
        self.__cliente = estado.contrato.cliente
        self.__data = estado.contrato.data
        self.__tipo = estado.contrato.tipo

class Estado():
    def __init__(self, contrato):
        self.__contrato = contrato
        
    @property
    def contrato(self):
        return self.__contrato

class Historico(object):

    def __init__(self):
        self.__estados_salvos = []

    @property
    def estados(self):
        return self.__estados_salvos

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)

if __name__ == '__main__':

    historico = Historico()

    contrato = Contrato(
        data=date.today(),
        cliente='Flávio Almeida'
    )

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.cliente = 'Jorge'

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    for estado in historico.estados:
        print(estado.contrato.cliente)