import pandas as pd
import json


def dados_lixeiras(all_data):
    # Converte o JSON para um DataFrame do Pandas
    all_data = pd.DataFrame(json.loads(all_data))

    # Pegando especificamente os dados do produto "Lixeira"
    lixeira_data = all_data[all_data["nome"] == "Lixeira"]

    # Ordenando o DataFrame pelo valor da variÃ¡vel "mes"
    lixeira_data = lixeira_data.sort_values(by="mes")

    return lixeira_data.to_json(orient="records")
