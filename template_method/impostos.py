from abc import ABCMeta, abstractmethod
class Template_imposto_condicional():

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if (self.deve_usar_maxima_taxacao(orcamento)):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)
    
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass
        
class ICPP(Template_imposto_condicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500
    
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07
    
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05
            
class IKCV(Template_imposto_condicional):        
    def deve_usar_maxima_taxacao(self, orcamento):
        tem_item_maior_que_cem_reais = self.__tem_item_maior_que_cem_reais(orcamento)
        
        return orcamento.valor > 500 and tem_item_maior_que_cem_reais
    
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1
    
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_cem_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if (item.valor > 100):
                return True
        return False