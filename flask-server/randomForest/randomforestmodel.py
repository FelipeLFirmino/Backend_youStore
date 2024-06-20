from sklearn.ensemble import RandomForestRegressor
import json
import pandas as pd
from decimal import Decimal  # Importe a classe Decimal corretamente

def prever_media_vendas(produto_data):
    # Converte o JSON para um DataFrame do Pandas
    produto_data = pd.DataFrame(produto_data)

    # Renomear o id referente as colunas para ser pelos nomes delas
    produto_data = produto_data.rename(columns={3: 'quantidade', 4: 'reposicao', 5: 'media_vendas', 7: 'preco_venda'})

    # Converter valores do DataFrame de Decimal para float
    produto_data = produto_data.applymap(lambda x: float(x) if isinstance(x, Decimal) else x)
    
    # Convertendo para numpy arrays
    X = produto_data[['quantidade', 'reposicao', 'preco_venda']].values
    X = X[:int(len(produto_data)-1)]
    y = produto_data['media_vendas'].values
    y = y[:int(len(produto_data)-1)]

    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)

   # Prevê a média de vendas do último mês
    dados_do_ultimo_mes = produto_data[['quantidade', 'reposicao', 'preco_venda']].tail(1)
    prediction = modelo.predict(dados_do_ultimo_mes)
    
# Converter o array NumPy em uma lista antes de serializar para JSON
    prediction_list = prediction.tolist()
    
# Certificar que todos os elementos da lista são do tipo float
    prediction_list = [float(i) for i in prediction_list]
    
    return json.dumps(prediction_list)