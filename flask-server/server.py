from flask import Flask, jsonify, request
import json

app = Flask(__name__)




def ler_arquivo(arquivo):
    produtos = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            linha = linha.strip()
            if linha:
                try:
                    produto = json.loads(linha)
                    # Adicionar valores para cálculo de lucratividade e reabastecimento
                    produto['preco_compra'] = produto['preco_compra']  
                    produto['preco_venda'] = produto['preco_venda'] 
                    produto['quantidade_vendida'] = produto['media_vendas']
                    produtos.append(produto)
                except json.JSONDecodeError:
                    print(f"Aviso: Ignorando linha mal formatada no arquivo: {linha}")
    return produtos



arquivo = 'C:/Users/lipe7/OneDrive/Documentos/GitHub/Backend_youStore/produtos.txt'  # nome do arquivo txt
produtos = ler_arquivo(arquivo)


@app.route('/listar_produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)
