import json
import pandas as pd

def dados_computadores(all_data):
    # Converte o JSON para um DataFrame do Pandas
    all_data = pd.DataFrame(json.loads(all_data))
    
    # Pegando especificamente os dados do produto "Computador"
    computador_data = all_data[all_data['nome'] == "Computador"]

    # Ordenando o DataFrame pelo valor da variÃ¡vel "mes"
    computador_data = computador_data.sort_values(by='mes')

    return computador_data.to_json(orient='records')