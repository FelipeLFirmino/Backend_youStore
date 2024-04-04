from flask import Flask, jsonify, request
from sklearn.ensemble import RandomForestRegressor
from ler_arquivo import ler_arquivo
from listar_produtos import listar_produtos
from prever_demanda import prever_demanda
from prever_demanda_individual import prever_demanda_individual
from calcular_lucratividade import calcular_lucratividade
from verificar_reabastecimento import verificar_reabastecimento
from calcular_media_vendas import calcular_media_vendas

app = Flask(__name__)

arquivo = 'produtos.txt'  # nome do arquivo txt
produtos = ler_arquivo(arquivo)

# treinamento do modelo RandomForestRegressor
X = []
y = []
for p in produtos:
    X.append([p['quantidade'], p['reposicao'], p['media_vendas']])
    y.append(p['demanda'])

modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X, y)

@app.route('/listar_produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/selecionar_produto/<int:id>', methods=['GET'])
def selecionar_produto(id):
    for produto in produtos:
        if produto['id'] == id:
            return jsonify(produto)
    return jsonify({'message': 'Produto não encontrado'}), 404

@app.route('/prever_demanda', methods=['POST'])
def prever_demanda():
    data = request.json
    produto_id = data.get('produto_id')
    for produto in produtos:
        if produto['id'] == produto_id:
            previsao = prever_demanda_individual(produto, produtos, modelo)
            return jsonify({'previsao_demanda': previsao})
    return jsonify({'message': 'Produto não encontrado'}), 404

@app.route('/calcular_lucratividade/<int:id>', methods=['GET'])
def calcular_lucratividade(id):
    for produto in produtos:
        if produto['id'] == id:
            lucratividade = calcular_lucratividade(produto['preco_compra'], produto['preco_venda'], produto['demanda'], produto['media_vendas'])
            return jsonify({'lucratividade': lucratividade})
    return jsonify({'message': 'Produto não encontrado'}), 404

@app.route('/verificar_reabastecimento/<int:id>', methods=['GET'])
def verificar_reabastecimento(id):
    for produto in produtos:
        if produto['id'] == id:
            verificar_reabastecimento(produto['quantidade'], produto['demanda'], produto['media_vendas'])
            return jsonify({'message': 'Verificação de reabastecimento concluída'})
    return jsonify({'message': 'Produto não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
