import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor



data_month1 = pd.read_csv('produtos.txt')
data_month2 = pd.read_csv('produtos2.txt')
data_month3 = pd.read_csv('produtos3.txt')
data_month4 = pd.read_csv('produtos4.txt')
data_month5 = pd.read_csv('produtos5.txt')
data_month6 = pd.read_csv('produtos6.txt')

# Combinar os dados em um único DataFrame
all_data = pd.concat([data_month1, data_month2, data_month3, data_month4, data_month5,data_month6], ignore_index=True)


# treinamento do modelo RandomForestRegressor
# convertendo para numpy arrays
X = all_data[['quantidade', 'media_vendas']].values
y = all_data['reposicao'].values


modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X, y)