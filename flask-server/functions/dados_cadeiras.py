import json
import pandas as pd


def dados_cadeiras(all_data):
    # Converte o JSON para um DataFrame do Pandas
    all_data = pd.DataFrame(json.loads(all_data))

    # Pegando especificamente os dados do produto "Cadeira"
    cadeira_data = all_data[all_data["nome"] == "Cadeira"]

    # Ordenando o DataFrame pelo valor da variÃ¡vel "mes"
    cadeira_data = cadeira_data.sort_values(by="mes")

    return cadeira_data.to_json(orient="records")
