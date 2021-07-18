from abc import ABCMeta, abstractmethod

class Expressao():
    __metaclass__ = ABCMeta

    @abstractmethod
    def avalia(self):
        pass

class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

class Soma(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita
    
    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()
        
class Numero(Expressao):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

if __name__ == '__main__':
    exp_esquerda = Soma(Numero(10), Numero(20))
    exp_direita = Subtracao(Numero(5), Numero(4))
    exp_final = Soma(exp_esquerda, exp_direita)
    print(exp_final.avalia())