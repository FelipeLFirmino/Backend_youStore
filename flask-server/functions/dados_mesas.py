import json
import pandas as pd


def dados_mesas(all_data):
     # Converte o JSON para um DataFrame do Pandas
    all_data= pd.DataFrame(json.loads(all_data))
    # Pegando especificamente os dados do produto "Mesa"
    mesa_data = all_data[all_data['nome'] == "Mesa"]

    # Ordenando o DataFrame pelo valor da variável "mes"
    mesa_data = mesa_data.sort_values(by='mes')

    return mesa_data.to_json(orient='records')