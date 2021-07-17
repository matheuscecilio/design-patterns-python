from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto
class Calculador_de_descontos():
    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        ).calcula(orcamento)

        return desconto

if __name__ == '__main__':
    import os, sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

    from orcamento import Orcamento
    from item import Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 1', 100))
    orcamento.adiciona_item(Item('Item 2', 600))
    orcamento.adiciona_item(Item('Item 3', 300))

    print (orcamento.valor)

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)

    print (f'O desconto foi de {desconto}')