import json
from application import app
from application.model.dao.produtosDao import ProdutoDao
from flask import render_template, request, url_for, redirect
from application.model.entity.produtos import Produtos


@app.route("/")
def home():
    lista_produtos = ProdutoDao().get_exibir_listaProdutos()
    return render_template("index.html", lista_produtos = lista_produtos)