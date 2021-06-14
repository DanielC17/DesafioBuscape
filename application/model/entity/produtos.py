class Produtos :
    def __init__(self, id, nome, imagem, valor, parcela, valorParcela):
        self._id = id
        self._nome = nome
        self._imagem = imagem
        self._valor = valor
        self._parcela = parcela
        self._valorParcela = valorParcela


    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_imagem(self):
        return self._imagem

    def get_valor(self):
        return self._valor

    def get_parcela(self):
        return self._parcela

    def get_valorParcela(self):
        return self._valorParcela

