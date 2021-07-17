from impostos import ISS, ICMS, ICPP, IKCV

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
    orcamento.adiciona_item(Item('Item 1', 50))
    orcamento.adiciona_item(Item('Item 2', 200))
    orcamento.adiciona_item(Item('Item 3', 250))

    print('ICMS')
    calculador.realiza_calculo(orcamento, ICMS())
    print('ISS')
    calculador.realiza_calculo(orcamento, ISS())
    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ICMS(ISS()))
    
    print('ICPP')
    calculador.realiza_calculo(orcamento, ICPP())
    print('IKCV')
    calculador.realiza_calculo(orcamento, IKCV())
    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
