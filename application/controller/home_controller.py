import json
from application import app
from application.model.dao.produtosDao import ProdutoDao
from flask import render_template, request, url_for, redirect

produtosDao = ProdutoDao()
lista_carrinho = produtosDao.lista_carrinho()
lista_produtos = produtosDao.get_exibir_listaProdutos()


@app.route("/")
def index():
    return render_template("index.html", lista_produtos = lista_produtos, lista_carrinho = lista_carrinho)


@app.route("/inserir/<id>")
def inserir(id):
    for i in lista_produtos:
        if int(id) == i.get_id():
            lista_carrinho.append(i)
            return redirect(url_for('index'))


@app.route("/excluir/<id>")
def excluir(id):
    for i in lista_carrinho:
        if int(id) == i.get_id():
            lista_carrinho.remove(i)
            return redirect(url_for('index'))
