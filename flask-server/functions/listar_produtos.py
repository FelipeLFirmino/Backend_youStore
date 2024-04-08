def listar_produtos(produtos):
    print("Lista de Produtos:")
    for idx, produto in enumerate(produtos, 1):
        print(f"{idx}. {produto['nome']}")