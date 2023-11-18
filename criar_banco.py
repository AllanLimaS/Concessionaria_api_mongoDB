#pip install pymongo

from pymongo import MongoClient

# Conecte-se ao servidor MongoDB (por padrão, em localhost:27017)
cliente = MongoClient('mongodb://localhost:27017/')

# Crie ou acesse um banco de dados (substitua 'nome_do_banco' pelo nome desejado)
banco_de_dados = cliente['Concessionaria']


colecao_carro = banco_de_dados['Carro']
colecao_marca = banco_de_dados['Marca']
colecao_modelo = banco_de_dados['Modelo']

print("Banco de dados e coleção criados com sucesso.")