# importar essa função na server.py e se certificar que ela esta mostrando TODOS os produtos separados pelo mes
# LEMBRANDO QUE ESSA FUNÇÃO PRECISA DOS PRODUTOS LIDOS PELA FUNÇÃO NO ARQUIVI "LER ARQUIVO"
def listar_produtos(produtos):
    print("Lista de Produtos:")
    for idx, produto in enumerate(produtos, 1):
        print(f"{idx}. {produto['nome']}")