from abc import ABCMeta, abstractmethod

class Expressao():
    __metaclass__ = ABCMeta

    @abstractmethod
    def avalia(self):
        pass
    
    @abstractmethod
    def aceita(self, visitor):
        pass

class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda
        
    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

class Soma(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda
        
    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()
    
    def aceita(self, visitor):
        visitor.visita_soma(self)
        
class Numero(Expressao):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero
        
    def aceita(self, visitor):
        visitor.visita_numero(self)

if __name__ == '__main__':
    expressao_1 = Soma(Numero(10), Numero(20))
    expressao_2 = Subtracao(Numero(5), Numero(4))
    expressao_3 = Subtracao(expressao_1, expressao_2)
    expressao_4 = Subtracao(Numero(45), Numero(74))
    expressao_5 = Soma(expressao_4, Numero(9))
    expressao_final = Soma(expressao_3, expressao_5)

    from impressao import Impressao

    impressao = Impressao()
    expressao_final.aceita(impressao)
    resultado = expressao_final.avalia()
    print(f' = {resultado}')

    