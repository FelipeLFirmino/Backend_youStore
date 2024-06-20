# from sklearn.ensemble import RandomForestRegressor
# import json
# import pandas as pd

# def prever_media_vendas(produto_data):
#     # Converte o JSON para um DataFrame do Pandas
#     produto_data = pd.DataFrame(json.loads(produto_data))

#     # Convertendo para numpy arrays
#     X = produto_data[['quantidade', 'reposicao', 'preco_venda']].values
#     X = X[:int(len(produto_data)-1)]
#     y = produto_data['media_vendas'].values
#     y = y[:int(len(produto_data)-1)]

#     modelo = RandomForestRegressor(n_estimators=100, random_state=42)
#     modelo.fit(X, y)

#     # Prevê a média de vendas do último mês, nesse caso o 12
#     dados_do_ultimo_mes = produto_data[['quantidade', 'reposicao', 'preco_venda']].tail(1)
#     prediction = modelo.predict(dados_do_ultimo_mes)

#     # Retorna diretamente o valor único da previsão
#     return float(prediction[0])  # Converte para float se necessário


from sklearn.ensemble import RandomForestRegressor
import json
import pandas as pd

def prever_media_vendas(produto_data):
# treinamento do modelo RandomForestRegressor com os dados do dataset lixeira
   
    

    #  Converte o JSON para um DataFrame do Pandas
    produto_data= pd.DataFrame(produto_data)
    

    # convertendo para numpy arrays
    X = produto_data[[3, 4,7]].values
    X = X[:int(len(produto_data)-1)]
    y = produto_data[5].values
    y = y[:int(len(produto_data)-1)]


    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)

    # preve a media de vendas do ultimo mes, nesse caso o 12
    dados_do_ultimo_mes = produto_data[[3, 4, 7]].tail(1)
    prediction = modelo.predict(dados_do_ultimo_mes)
    
     # Converter o array NumPy em uma lista antes de serializar para JSON
    prediction_list = prediction.tolist()
    return json.dumps(prediction_list)

  