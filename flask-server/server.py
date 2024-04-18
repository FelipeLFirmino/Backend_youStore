from flask import Flask, jsonify, request
from functions import ler_arquivos
from functions import dados_mesas
from functions import dados_computadores
from functions import dados_teclados
from functions import dados_lixeiras
from functions import dados_cadeiras



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


# @app.route('/caminho_listar_produtos', methods=['GET'])
# def caminho_listar_produtos():
#     produtos = ler_arquivos(pasta)
#     # Converte o DataFrame em um dicionário para serialização JSON
#     produtos_dict = produtos.to_dict(orient='records')
#     return jsonify(produtos_dict)











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
