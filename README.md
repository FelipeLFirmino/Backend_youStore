# Backend YouStore

O Backend YouStore é uma API desenvolvida com Flask, Python, que utiliza a biblioteca Pandas para manipulação de dados e Scikit-learn para aplicar o algoritmo de Random Forest. Este backend lê dados de arquivos .txt que simulam um banco de dados e prevê a média de vendas para o próximo mês de uma loja de varejo.

## Tabela de Conteúdos

- [Descrição](#descrição)
- [Instalação](#instalação)
- [Uso](#uso)
- [Autores](#autores)

## Descrição

O Backend YouStore é responsável por processar e analisar dados de vendas de uma loja de varejo. Utilizando a biblioteca Pandas, os dados são manipulados para serem utilizados no modelo de Machine Learning implementado com Scikit-learn. O modelo de Random Forest é usado para prever a média de vendas para o próximo mês, fornecendo insights valiosos para a tomada de decisões.

* Todos os dados contidos nos arquivos .txt mencionados estão sendo agora processados diretamente em um banco de dados dedicado para aplicação, implantado e gerenciado no console da Amazon RDS - AWS. *

## Instalação

Para rodar o servidor localmente, siga os passos abaixo:

1. Clone o repositório:
   git clone https://github.com/seu-usuario/backend-youstore.git

2. Navegue até o diretório do projeto:
   cd flask-server

3. Crie um ambiente virtual e ative-o:
   python -m venv venv
   venv\Scripts\activate
   source venv/bin/activate

4. Instale as dependências:
   pip install -r requirements.txt

5.Inicie o servidor:

python server.py

O servidor estará disponível em http://localhost:5000.

## Autores

Felipe Firmino- Desenvolvedor Principal

Bruno Sandes- Cientista de dados

Gabriel vangasse- Desenvolvedor

Sergio - Desenvolvedor
