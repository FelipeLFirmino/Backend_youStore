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
import os
from dotenv import load_dotenv
load_dotenv()



# CONEXÃO BANCO DE DADOS
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE"),
        port=os.getenv("DB_PORT"),
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


@app.route("/quantidade_vendas_mes11", methods=["GET"])
def quantidade_vendas_mes11():
    connection = None
    try:
        connection = get_connection()
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            sql = "SELECT nome, media_vendas FROM produtos WHERE mes = 11"
            cursor.execute(sql)
            produtos_mes11 = cursor.fetchall()
            # Montar o resultado como um dicionário
            resultado = {
                produto["nome"]: produto["media_vendas"] for produto in produtos_mes11
            }
    except Exception as e:
        print(f"Erro ao consultar o banco de dados: {e}")
        resultado = {}
    finally:
        if connection:
            connection.close()
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)
