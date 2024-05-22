# Lista de produtos do arquivo
produtos_verificar = [
    {"id": 1, "nome": "Lixeira", "mes": 1, "quantidade": 50, "reposicao": 10, "media_vendas": 25, "preco_compra": 15, "preco_venda": 35},
    {"id": 2, "nome": "Cadeira", "mes": 1, "quantidade": 120, "reposicao": 10, "media_vendas": 50, "preco_compra": 30, "preco_venda": 80},
    {"id": 3, "nome": "Mesa", "mes": 1, "quantidade": 170, "reposicao": 10, "media_vendas": 40, "preco_compra": 50, "preco_venda": 120},
    {"id": 4, "nome": "Computador", "mes": 1, "quantidade": 110, "reposicao": 10, "media_vendas": 80, "preco_compra": 200, "preco_venda": 600},
    {"id": 5, "nome": "Teclado", "mes": 1, "quantidade": 135, "reposicao": 10, "media_vendas": 65, "preco_compra": 25, "preco_venda": 50},
]

def test_verificar_produtos():
    # Cópia para comparação
    #Se alterar valores e ou adicionar produtos em um e não tiver no outro irá dar erro no teste
    produtos_lidos = [
        {"id": 1, "nome": "Lixeira", "mes": 1, "quantidade": 50, "reposicao": 10, "media_vendas": 25, "preco_compra": 15, "preco_venda": 35},
        {"id": 2, "nome": "Cadeira", "mes": 1, "quantidade": 120, "reposicao": 10, "media_vendas": 50, "preco_compra": 30, "preco_venda": 80},
        {"id": 3, "nome": "Mesa", "mes": 1, "quantidade": 170, "reposicao": 10, "media_vendas": 40, "preco_compra": 50, "preco_venda": 120},
        {"id": 4, "nome": "Computador", "mes": 1, "quantidade": 110, "reposicao": 10, "media_vendas": 80, "preco_compra": 200, "preco_venda": 600},
        {"id": 5, "nome": "Teclado", "mes": 1, "quantidade": 135, "reposicao": 10, "media_vendas": 65, "preco_compra": 25, "preco_venda": 50}
    ]

    # Verifica as listas e se tiver alguma coisa diferente da erro, se não tiver mostra mensagem de sucesso
    for produto in produtos_verificar:
        assert produto in produtos_lidos

    
    for produto in produtos_lidos:
        assert produto in produtos_verificar

    # Imprimir mensagem de sucesso
    print("Todos os produtos estão presentes!")

# Chamar o teste
test_verificar_produtos()