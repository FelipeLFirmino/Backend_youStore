from flask import Flask, jsonify, request
import json


app = Flask(__name__)


# essas sao as rotas do backend elas devem ser criadas com nomes intuitivos e as funções importadas colocadas aqui
# NAO COLOCAR FUNÇOES DIRETAMENTE NESSE ARQUIVO
@app.route('/listar_produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/ler_arquivo', methods=['GET'])
def ler_arquivo():
    return jsonify(produtos)


if __name__ == "__main__":
    app.run(debug=True)
