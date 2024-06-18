import pandas as pd
import psycopg2
import os
from io import StringIO

# Configuração de conexão com o banco de dados
db_config = {
    'host': os.getenv('DB_HOST'), # you-store.c7k26sugsa4x.us-east-1.rds.amazonaws.com
    'dbname': os.getenv('DB_NAME'), # you-store
    'user': os.getenv('DB_USER'), # postgres
    'password': os.getenv('DB_PASSWORD'), # projeto123
    'port': os.getenv('DB_PORT', 5432)
}

def ler_arquivo(pasta):
    lista_dataframes = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'r') as file:
                linhas = file.readlines()
                for num_linha, linha in enumerate(linhas, start=1):
                    try:
                        dataframe = pd.read_json(StringIO(linha), lines=True)
                        lista_dataframes.append(dataframe)
                    except ValueError as e:
                        print(f"Erro na linha {num_linha} do arquivo {arquivo}: {e}")
    all_data = pd.concat(lista_dataframes, ignore_index=True)
    return all_data

def inserir_dados(db_conn, dados):
    cursor = db_conn.cursor()
    for index, linha in dados.iterrows():
        try:
            cursor.execute(
                """
                INSERT INTO produtos (id, nome, mes, quantidade, reposicao, media_vendas, preco_compra, preco_venda)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id, mes) 
                DO UPDATE SET 
                    nome = EXCLUDED.nome,
                    quantidade = EXCLUDED.quantidade,
                    reposicao = EXCLUDED.reposicao,
                    media_vendas = EXCLUDED.media_vendas,
                    preco_compra = EXCLUDED.preco_compra,
                    preco_venda = EXCLUDED.preco_venda
                """,
                (linha['id'], linha['nome'], linha['mes'], linha['quantidade'], linha['reposicao'], linha['media_vendas'], linha['preco_compra'], linha['preco_venda'])
            )
        except Exception as e:
            print(f"Erro ao inserir dados na linha {index}: {e}")
            db_conn.rollback()
    db_conn.commit()
    cursor.close()

# Caminho para a pasta contendo os arquivos de dados
pasta_dados = r'C:\Users\Bruno\Desktop\Programação\Backend_youStore-main\Backend_youStore-main\Data'

# Conectar ao banco de dados
try:
    db_conn = psycopg2.connect(**db_config)
except psycopg2.OperationalError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit(1)

# Ler os dados do arquivo e inserir no banco de dados
dados = ler_arquivo(pasta_dados)
inserir_dados(db_conn, dados)

# Fechar a conexão com o banco de dados
db_conn.close()
