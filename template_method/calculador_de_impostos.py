from impostos import ICPP, IKCV

class CalculadorDeImpostos():
    def realiza_calculo(self, orcamento, imposto):        
        imposto_calculado = imposto.calcula(orcamento)        
        print(imposto_calculado)

if __name__ == '__main__':
    import os, sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

    from orcamento import Orcamento
    from item import Item

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 100))
    # orcamento.adiciona_item(Item('Item 2', 200))
    # orcamento.adiciona_item(Item('Item 3', 50))
    
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())
