

from application.model.entity.produtos import Produtos
import json


class ProdutoDao:
    def __init__(self):
        self._carrinhoList = []
        self._listaProdutos = []

        with open('C:\\Users\\DKs\\Documents\\Projetos_GitHub\\DesafioBuscape\\application\\view\\static\\json\\produtos.json') as diretorio_produto:
            lista_produtos = json.load(diretorio_produto)

        for i in lista_produtos:
            self._listaProdutos.append(Produtos(i['id'], i['name'], i['images'], i['price']['value'], i['price']['installments'], i['price']['installmentValue']))

    def lista_carrinho(self):
        return self._carrinhoList

    def get_exibir_listaProdutos(self):
        return self._listaProdutos



