import pandas as pd
import os


def ler_arquivo(pasta):
    # Lista para armazenar os DataFrames de cada arquivo
    lista_dataframes = []

    # Iterar sobre os arquivos na pasta
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".txt"):
            # Caminho completo do arquivo
            caminho_arquivo = os.path.join(pasta, arquivo)
            # Ler o arquivo linha por linha
            with open(caminho_arquivo, "r") as file:
                linhas = file.readlines()
                # Iterar sobre as linhas e converter cada uma em um DataFrame
                for num_linha, linha in enumerate(linhas, start=1):
                    try:
                        # Carregar o JSON da linha em um DataFrame e adicionar à lista
                        dataframe = pd.read_json(linha, lines=True)
                        lista_dataframes.append(dataframe)
                    except ValueError as e:
                        print(f"Erro na linha {num_linha}: {e}")

    # Concatenar todos os DataFrames da lista em um único DataFrame
    all_data = pd.concat(lista_dataframes, ignore_index=True)
    # Converter o DataFrame para JSON e retorná-lo
    return all_data.to_json(orient="records")
