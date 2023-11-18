#pip install pymongo

from pymongo import MongoClient

# Conecte-se ao servidor MongoDB (por padrão, em localhost:27017)
cliente = MongoClient('mongodb://localhost:27017/')

# Crie ou acesse um banco de dados (substitua 'nome_do_banco' pelo nome desejado)
banco_de_dados = cliente['Concessionaria']


colecao_carro = banco_de_dados['carro']
colecao_loja = banco_de_dados['loja']
colecao_modelo = banco_de_dados['modelo']

print("Banco de dados e coleção criados com sucesso.")