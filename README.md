# Concessionaria_api_mongoDB

Projeto desenvolvido para disciplina de Banco de Dados 2 da UNIVALI. 
Onde tem como objetivo implementar três CRUDs com persistência de dados em banco de dados não relacional orientado a documentos, o escolhido para esse trabalho foi o MongoDB.

Foi fornecido o diagrama de classes a seguir para utilizar de referência. 

<p align="center">
    <img src="https://github.com/AllanLimaS/Concessionaria_api_mongoDB/assets/49033925/ba88d69f-a44b-4ee3-a060-c61bc17e3537">
</p>

## Desenvolvimento

Os bancos de dados não relacionais são orientados a documentos e seus conjuntos do documentos, são definidos como coleções, o que seria análogo a tabelas, nos bancos de dados não relacionais. Dessa forma, nesse trabalho foram criados três coleções, são elas: _(i)_ Carro; _(ii)_ Modelo e _(iii)_ Marca. 

## Como executar

Para executar o projeto, basta baixar o mongoDB, iniciar uma conexão com ele.

baixar as dependências: 
pip install Flask
pip install pymongo

Executar o script "criar_banco.py" e após isso o script "app.py". 

Com a api rodando, basta utilizar os endpoints fornecidos, em algum software como postman. 
