import json
# importar essa funcao no server.py e fazer com que ela leia todos os txt
# LEMBRANDO QUE ESSA FUNÇÃO PRECISA IMPORTAR OS ARQUIVOS DE TEXTO e SEUS RESPECTIVOS CAMINHOS (ELES ESTAO NA PASTA DATA AGR)
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