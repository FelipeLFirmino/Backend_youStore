from flask import Flask, jsonify, request
from functions import ler_arquivos


app = Flask(__name__)


# essas sao as rotas do backend elas devem ser criadas com nomes intuitivos e as funções importadas colocadas aqui
# NAO COLOCAR FUNÇOES DIRETAMENTE NESSE ARQUIVO
# @app.route('/listar_produtos', methods=['GET'])
# def listar_produtos():
#     return jsonify(produtos)

 # Pasta onde estão os arquivos JSON
pasta = 'C:/Users/lipe7/OneDrive/Documentos/GitHub/Backend_youStore/Data'

@app.route('/caminho_ler_arquivos', methods=['GET'])
def caminho_ler_arquivos():
    return ler_arquivos(pasta)












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
