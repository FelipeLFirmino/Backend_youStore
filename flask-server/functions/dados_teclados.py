import pandas as pd
import json


def dados_teclados(all_data):

    # Converte o JSON para um DataFrame do Pandas
    all_data = pd.DataFrame(json.loads(all_data))

    # Pegando especificamente os dados do produto "Teclado"
    teclado_data = all_data[all_data["nome"] == "Teclado"]

    # Ordenando o DataFrame pelo valor da variÃ¡vel "mes"
    teclado_data = teclado_data.sort_values(by="mes")

    return teclado_data.to_json(orient="records")
