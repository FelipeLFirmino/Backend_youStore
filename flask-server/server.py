from flask import Flask, jsonify
import json
from functions import (
    ler_arquivos,
    dados_mesas,
    dados_computadores,
    dados_teclados,
    dados_lixeiras,
    dados_cadeiras,
)
from randomForest import randomforestmodel
import psycopg2
import psycopg2.extras


# CONEXÃO BANCO DE DADOS
def get_connection():
    return psycopg2.connect(
        host="you-store.c7k26sugsa4x.us-east-1.rds.amazonaws.com",
        user="postgres",
        password="projeto123",
        database="banco-de-dados-youStore",
        port=5432,
    )


app = Flask(__name__)


# VER TODOS OS PRODUTOS
@app.route("/caminho_ler_produtos", methods=["GET"])
def caminho_ler_produtos():
    connection = None
    try:
        connection = get_connection()
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            sql = "SELECT * FROM produtos"
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")
        result = []
    finally:
        if connection:
            connection.close()
    return jsonify(result)


def ler_dados_produto(nome_produto):
    connection = None
    try:
        connection = get_connection()
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            sql = "SELECT * FROM produtos WHERE nome = %s"
            cursor.execute(sql, (nome_produto,))
            result = cursor.fetchall()
    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")
        result = []
    finally:
        if connection:
            connection.close()
    return result


# REQUISIÇÕES PRODUTOS
@app.route("/caminho_ler_mesas", methods=["GET"])
def caminho_ler_mesas():
    dados_json_mesa = ler_dados_produto("Mesa")
    return jsonify(dados_json_mesa)


@app.route("/caminho_ler_computadores", methods=["GET"])
def caminho_ler_computadores():
    dados_json_computadores = ler_dados_produto("Computador")
    return jsonify(dados_json_computadores)


@app.route("/caminho_ler_teclados", methods=["GET"])
def caminho_ler_teclados():
    dados_json_teclado = ler_dados_produto("Teclado")
    return jsonify(dados_json_teclado)


@app.route("/caminho_ler_lixeiras", methods=["GET"])
def caminho_ler_lixeiras():
    dados_json_lixeira = ler_dados_produto("Lixeira")
    return jsonify(dados_json_lixeira)


@app.route("/caminho_ler_cadeiras", methods=["GET"])
def caminho_ler_cadeiras():
    dados_json_cadeira = ler_dados_produto("Cadeira")
    return jsonify(dados_json_cadeira)


# REQUISIÇÕES DEMANDAS


@app.route("/caminho_prever_demanda_produto/<string:produto>", methods=["GET"])
def caminho_prever_demanda_produto(produto):
    if produto not in ["Computador", "Mesa", "Cadeira", "Teclado", "Lixeira"]:
        return jsonify({"erro": "Produto não reconhecido!"})

    dados_produto = ler_dados_produto(produto)
    previsao = randomforestmodel.prever_media_vendas(dados_produto)
    return jsonify({f"previsao_{produto}": previsao})


@app.route("/caminho_prever_demanda_produto/todos_produtos", methods=["GET"])
def caminho_prever_demanda_todos_produtos():
    previsoes_todos_produtos = {}

    for produto in ["Computador", "Mesa", "Cadeira", "Teclado", "Lixeira"]:
        dados_produto = ler_dados_produto(produto)
        previsao = randomforestmodel.prever_media_vendas(dados_produto)
        previsoes_todos_produtos[produto] = previsao

    return jsonify(previsoes_todos_produtos)


if __name__ == "__main__":
    app.run(debug=True)
