from datetime import date

class Item():
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor
    
class Nota_fiscal():
    def __init__(self, razao_social, cnpj, itens, data_de_emissao = date.today(), detalhes = ''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao

        if (len(detalhes) > 20):
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')

        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social
        
    @property
    def cnpj(self):
        return self.__cnpj
        
    @property
    def data_de_emissao(self):
        return self.__data_de_emissao
        
    @property
    def detalhes(self):
        return self.__detalhes
        
    @property
    def itens(self):
        return self.__itens

if __name__ == '__main__':
    itens = [
        Item('Item A', 100),
        Item('Item B', 200),
        Item('Item C', 300),
    ]

    from nota_fiscal_builder import Nota_fiscal_builder

    nota_fiscal = (Nota_fiscal_builder()
        .com_razao_social('MATS LTDA')
        .com_cnpj('0123456789')
        .com_itens(itens)
        .build())