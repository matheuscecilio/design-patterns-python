from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento():
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass
    
    @abstractmethod
    def aprova(self, orcamento):
        pass
    
    @abstractmethod
    def reprova(self, orcamento):
        pass
    
    @abstractmethod
    def finaliza(self, orcamento):
        pass

class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
        
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()
        
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()
        
    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não podem ir para finalizado')

class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
    
    def aprova(self, orcamento):
        raise Exception('Orçamento já está aprovado')
        
    def reprova(self, orcamento):
        raise Exception('Orçamentos aprovados não podem ser reprovados')
        
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não receberam desconto extra')
    
    def aprova(self, orcamento):
        raise Exception('Orçamentos reprovados não podem ser aprovados')
        
    def reprova(self, orcamento):
        raise Exception('Orçamento já está reprovado')
        
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalzados não receberam desconto extra')
    
    def aprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser aprovados')
        
    def reprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser reprovados')
        
    def finaliza(self, orcamento):
        raise Exception('Orçamento já está finalizado')

class Orcamento():
    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(orcamento)
        
    def reprova(self):
        self.estado_atual.reprova(orcamento)
        
    def finaliza(self):
        self.estado_atual.finaliza(orcamento)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(orcamento)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def total_itens(self):
        return len(self.__itens)

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

if (__name__ == '__main__'):
    import os, sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)
    from item import Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 50))
    orcamento.adiciona_item(Item('Item 2', 200))
    orcamento.adiciona_item(Item('Item 3', 250))

    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)