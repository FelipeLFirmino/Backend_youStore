from flask import Flask, jsonify, request
from functions import ler_arquivos
from functions import dados_mesas
from functions import dados_computadores
from functions import dados_teclados
from functions import dados_lixeiras
from functions import dados_cadeiras
from randomForest import randomforestmodel



app = Flask(__name__)


# essas sao as rotas do backend elas devem ser criadas com nomes intuitivos e as funções importadas colocadas aqui
# NAO COLOCAR FUNÇOES DIRETAMENTE NESSE ARQUIVO

pasta = 'C:/Users/lipe7/OneDrive/Documentos/GitHub/Backend_youStore/Data'

@app.route('/caminho_ler_arquivos', methods=['GET'])
def caminho_ler_arquivos():
    dados_json = ler_arquivos.ler_arquivo(pasta)
    return jsonify(dados_json)


@app.route('/caminho_ler_mesas', methods=['GET'])
def caminho_ler_mesas():
    dados_json = ler_arquivos.ler_arquivo(pasta)
    dados_json_mesa = dados_mesas.dados_mesas(dados_json)
    return jsonify(dados_json_mesa)

@app.route('/caminho_ler_computadores', methods=['GET'])
def caminho_ler_computadores():
    dados_json = ler_arquivos.ler_arquivo(pasta)
    dados_json_computadores = dados_computadores.dados_computadores(dados_json)
    return jsonify(dados_json_computadores)

@app.route('/caminho_ler_teclados', methods=['GET'])
def caminho_ler_teclados():
    dados_json = ler_arquivos.ler_arquivo(pasta)
    dados_json_teclado = dados_teclados.dados_teclados(dados_json)
    return jsonify(dados_json_teclado)

@app.route('/caminho_ler_lixeiras', methods=['GET'])
def caminho_ler_lixeiras():
    dados_json = ler_arquivos.ler_arquivo(pasta)
    dados_json_lixeira = dados_lixeiras.dados_lixeiras(dados_json)
    return jsonify(dados_json_lixeira)

@app.route('/caminho_ler_cadeiras', methods=['GET'])
def caminho_ler_cadeiras():
    dados_json = ler_arquivos.ler_arquivo(pasta)
    dados_json_cadeira = dados_cadeiras.dados_cadeiras(dados_json)
    return jsonify(dados_json_cadeira)


@app.route('/caminho_prever_demanda_produto/<string:produto>', methods=['GET'])
def caminho_prever_demanda_produto(produto):
    # Verificar se o produto fornecido está na lista de produtos permitidos
    if produto not in ['computador', 'mesa', 'cadeira', 'teclado', 'lixeira']:
        return jsonify({'erro': 'Produto não reconhecido!'})

    # Ler os dados do arquivo correspondente ao produto
    dados_json = ler_arquivos.ler_arquivo(pasta) 
    
    # Selecionar os dados específicos do produto
    if produto == 'computador':
        dados_produto = dados_computadores.dados_computadores(dados_json)
    elif produto == 'mesa':
        dados_produto = dados_mesas.dados_mesas(dados_json)
    elif produto == 'cadeira':
        dados_produto = dados_cadeiras.dados_cadeiras(dados_json)
    elif produto == 'teclado':
        dados_produto = dados_teclados.dados_teclados(dados_json)
    elif produto == 'lixeira':
        dados_produto = dados_lixeiras.dados_lixeiras(dados_json)

    # Treinar o modelo usando os dados do produto e obter a previsão
    previsao = randomforestmodel.prever_media_vendas(dados_produto)

    # Retornar a previsão para o produto específico
    return jsonify({f'previsao_{produto}': previsao})


@app.route('/caminho_prever_demanda_produto/todos_produtos', methods=['GET'])
def caminho_prever_demanda_todos_produtos():
    # Lista para armazenar as previsões de demanda de todos os produtos
    previsoes_todos_produtos = {}

    # Fazendo previsões de demanda para cada produto individualmente
    for produto in ['computador', 'mesa', 'cadeira', 'teclado', 'lixeira']:
        # Ler os dados do arquivo correspondente ao produto
        dados_json = ler_arquivos.ler_arquivo(pasta)

        # Selecionar os dados específicos do produto
        if produto == 'computador':
            dados_produto = dados_computadores.dados_computadores(dados_json)
        elif produto == 'mesa':
            dados_produto = dados_mesas.dados_mesas(dados_json)
        elif produto == 'cadeira':
            dados_produto = dados_cadeiras.dados_cadeiras(dados_json)
        elif produto == 'teclado':
            dados_produto = dados_teclados.dados_teclados(dados_json)
        elif produto == 'lixeira':
            dados_produto = dados_lixeiras.dados_lixeiras(dados_json)

            # Treinar o modelo usando os dados do produto e obter a previsão
        previsao = randomforestmodel.prever_media_vendas(dados_produto)

        # Adicionando a previsão do produto à lista
        previsoes_todos_produtos[produto] = previsao

    # Retornando as previsões de todos os produtos
    return jsonify(previsoes_todos_produtos)








# Adicionando novas approute aqui
# @app.route('/calcular_media_vendas', methods=['GET'])
# def calcular_media_vendas_route():
#     media_vendas = calcular_media_vendas(produtos)
#     return jsonify(media_vendas)

# @app.route('/calcular_lucratividade', methods=['POST'])
# def calcular_lucratividade_route():
#     dados = request.get_json()
#     preco_compra = dados['preco_compra']
#     preco_venda = dados['preco_venda']
#     demanda = dados['demanda']
#     media_vendas = dados['media_vendas']
    
#     lucratividade = calcular_lucratividade(preco_compra, preco_venda, demanda, media_vendas)
    
#     return jsonify({'lucratividade': lucratividade})

if __name__ == "__main__":
    app.run(debug=True)


#teste
