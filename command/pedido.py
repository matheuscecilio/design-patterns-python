from datetime import date

class Pedido():
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__pago = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente
        
    @property
    def valor(self):
        return self.__valor
        
    @property
    def status(self):
        return self.__status
        
    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

from abc import ABCMeta, abstractmethod

class Comando():
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass

class Conclui_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()
        
class Paga_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()

class Fila_de_trabalho():
    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()

if __name__ == '__main__':
    pedido_1 = Pedido('Matheus', 200)
    pedido_2 = Pedido('Pedro', 400)
    pedido_3 = Pedido('Juliano', 4040)

    fila_de_trabalho = Fila_de_trabalho()
    comando_1 = Conclui_pedido(pedido_1)
    comando_2 = Paga_pedido(pedido_1)
    comando_3 = Conclui_pedido(pedido_2)
    comando_4 = Conclui_pedido(pedido_3)

    fila_de_trabalho.adiciona(comando_1)
    fila_de_trabalho.adiciona(comando_2)
    fila_de_trabalho.adiciona(comando_3)
    fila_de_trabalho.adiciona(comando_4)

    fila_de_trabalho.processa()