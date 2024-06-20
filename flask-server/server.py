from flask import Flask, jsonify
import json
from functions import ler_arquivos, dados_mesas, dados_computadores, dados_teclados, dados_lixeiras, dados_cadeiras
from randomForest import randomforestmodel
import psycopg2
import psycopg2.extras


#CONEXÃO BANCO DE DADOS
def get_connection():
    return psycopg2.connect(
        host='you-store.c7k26sugsa4x.us-east-1.rds.amazonaws.com',
        user='postgres',
        password='projeto123',
        database='banco-de-dados-youStore',
        port=5432
    )


app = Flask(__name__)



#VER TODOS OS PRODUTOS
@app.route('/caminho_ler_produtos', methods=['GET'])
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

#REQUISIÇÕES PRODUTOS
@app.route('/caminho_ler_mesas', methods=['GET'])
def caminho_ler_mesas():
    dados_json_mesa = ler_dados_produto('Mesa')
    return jsonify(dados_json_mesa)

@app.route('/caminho_ler_computadores', methods=['GET'])
def caminho_ler_computadores():
    dados_json_computadores = ler_dados_produto('Computador')
    return jsonify(dados_json_computadores)

@app.route('/caminho_ler_teclados', methods=['GET'])
def caminho_ler_teclados():
    dados_json_teclado = ler_dados_produto('Teclado')
    return jsonify(dados_json_teclado)

@app.route('/caminho_ler_lixeiras', methods=['GET'])
def caminho_ler_lixeiras():
    dados_json_lixeira = ler_dados_produto('Lixeira')
    return jsonify(dados_json_lixeira)

@app.route('/caminho_ler_cadeiras', methods=['GET'])
def caminho_ler_cadeiras():
    dados_json_cadeira = ler_dados_produto('Cadeira')
    return jsonify(dados_json_cadeira)



@app.route('/caminho_prever_demanda_produto/<string:produto>', methods=['GET'])
def caminho_prever_demanda_produto(produto):
    if produto not in ['Computador', 'Mesa', 'Cadeira', 'Teclado', 'Lixeira']:
        return jsonify({'erro': 'Produto não reconhecido!'})

    dados_produto = ler_dados_produto(produto)
    previsao = randomforestmodel.prever_media_vendas(dados_produto)
    return jsonify({f'previsao_{produto}': previsao})

@app.route('/caminho_prever_demanda_produto/todos_produtos', methods=['GET'])
def caminho_prever_demanda_todos_produtos():
    previsoes_todos_produtos = {}

    for produto in ['Computador', 'Mesa', 'Cadeira', 'Teclado', 'Lixeira']:
        dados_produto = ler_dados_produto(produto)
        previsao = randomforestmodel.prever_media_vendas(dados_produto)
        previsoes_todos_produtos[produto] = previsao

    return jsonify(previsoes_todos_produtos)

if __name__ == "__main__":
    app.run(debug=True)













# essas sao as rotas do backend elas devem ser criadas com nomes intuitivos e as funções importadas colocadas aqui
# NAO COLOCAR FUNÇOES DIRETAMENTE NESSE ARQUIVO

# pasta = 'C:/Users/lipe7/OneDrive/Documentos/GitHub/Backend_youStore/Data'

# @app.route('/caminho_ler_arquivos', methods=['GET'])
# def caminho_ler_arquivos():
#     dados_json = ler_arquivos.ler_arquivo(pasta)
#     return jsonify(dados_json)


# @app.route('/caminho_ler_mesas', methods=['GET'])
# def caminho_ler_mesas():
#     dados_json = ler_arquivos.ler_arquivo(pasta)
#     dados_json_mesa = dados_mesas.dados_mesas(dados_json)
#     return jsonify(dados_json_mesa)

# @app.route('/caminho_ler_computadores', methods=['GET'])
# def caminho_ler_computadores():
#     dados_json = ler_arquivos.ler_arquivo(pasta)
#     dados_json_computadores = dados_computadores.dados_computadores(dados_json)
#     return jsonify(dados_json_computadores)

# @app.route('/caminho_ler_teclados', methods=['GET'])
# def caminho_ler_teclados():
#     dados_json = ler_arquivos.ler_arquivo(pasta)
#     dados_json_teclado = dados_teclados.dados_teclados(dados_json)
#     return jsonify(dados_json_teclado)

# @app.route('/caminho_ler_lixeiras', methods=['GET'])
# def caminho_ler_lixeiras():
#     dados_json = ler_arquivos.ler_arquivo(pasta)
#     dados_json_lixeira = dados_lixeiras.dados_lixeiras(dados_json)
#     return jsonify(dados_json_lixeira)

# @app.route('/caminho_ler_cadeiras', methods=['GET'])
# def caminho_ler_cadeiras():
#     dados_json = ler_arquivos.ler_arquivo(pasta)
#     dados_json_cadeira = dados_cadeiras.dados_cadeiras(dados_json)
#     return jsonify(dados_json_cadeira)


# @app.route('/caminho_prever_demanda_produto/<string:produto>', methods=['GET'])
# def caminho_prever_demanda_produto(produto):
#     # Verificar se o produto fornecido está na lista de produtos permitidos
#     if produto not in ['computador', 'mesa', 'cadeira', 'teclado', 'lixeira']:
#         return jsonify({'erro': 'Produto não reconhecido!'})

#     # Ler os dados do arquivo correspondente ao produto
#     dados_json = ler_arquivos.ler_arquivo(pasta) 
    
#     # Selecionar os dados específicos do produto
#     if produto == 'computador':
#         dados_produto = dados_computadores.dados_computadores(dados_json)
#     elif produto == 'mesa':
#         dados_produto = dados_mesas.dados_mesas(dados_json)
#     elif produto == 'cadeira':
#         dados_produto = dados_cadeiras.dados_cadeiras(dados_json)
#     elif produto == 'teclado':
#         dados_produto = dados_teclados.dados_teclados(dados_json)
#     elif produto == 'lixeira':
#         dados_produto = dados_lixeiras.dados_lixeiras(dados_json)

#     # Treinar o modelo usando os dados do produto e obter a previsão
#     previsao = randomforestmodel.prever_media_vendas(dados_produto)

#     # Retornar a previsão para o produto específico
#     return jsonify({f'previsao_{produto}': previsao})


# @app.route('/caminho_prever_demanda_produto/todos_produtos', methods=['GET'])
# def caminho_prever_demanda_todos_produtos():
#     # Lista para armazenar as previsões de demanda de todos os produtos
#     previsoes_todos_produtos = {}

#     # Fazendo previsões de demanda para cada produto individualmente
#     for produto in ['computador', 'mesa', 'cadeira', 'teclado', 'lixeira']:
#         # Ler os dados do arquivo correspondente ao produto
#         dados_json = ler_arquivos.ler_arquivo(pasta)

#         # Selecionar os dados específicos do produto
#         if produto == 'computador':
#             dados_produto = dados_computadores.dados_computadores(dados_json)
#         elif produto == 'mesa':
#             dados_produto = dados_mesas.dados_mesas(dados_json)
#         elif produto == 'cadeira':
#             dados_produto = dados_cadeiras.dados_cadeiras(dados_json)
#         elif produto == 'teclado':
#             dados_produto = dados_teclados.dados_teclados(dados_json)
#         elif produto == 'lixeira':
#             dados_produto = dados_lixeiras.dados_lixeiras(dados_json)

#             # Treinar o modelo usando os dados do produto e obter a previsão
#         previsao = randomforestmodel.prever_media_vendas(dados_produto)

#         # Adicionando a previsão do produto à lista
#         previsoes_todos_produtos[produto] = previsao

#     # Retornando as previsões de todos os produtos
#     return jsonify(previsoes_todos_produtos)




# if __name__ == "__main__":
#     app.run(debug=True)


# #teste
