# Concessionaria_api_mongoDB

Projeto desenvolvido para disciplina de Banco de Dados 2 da UNIVALI. 
Onde tem como objetivo implementar três CRUDs com persistência de dados em banco de dados não relacional orientado a documentos, o escolhido para esse trabalho foi o MongoDB.

Foi fornecido o diagrama de classes a seguir para utilizar de referência. 

<p align="center">
    <img src="https://github.com/AllanLimaS/Concessionaria_api_mongoDB/assets/49033925/ba88d69f-a44b-4ee3-a060-c61bc17e3537">
</p>

## Desenvolvimento

Os bancos de dados não relacionais são orientados a documentos e seus conjuntos do documentos, são definidos como coleções, o que seria análogo a tabelas nos bancos de dados relacionais. Dessa forma, nesse trabalho foram criados três coleções, são elas: _(i)_ Carro; _(ii)_ Modelo e _(iii)_ Marca. 

As propriedades e métodos de cada coleção está presente no modelo de relações acima. Como cada coleção possui métodos distintos, foi optado por usar o modelo de referência ao invés do modelo "embarcado", que unifica todas as tabelas em uma só. O modelo de referência, por sua vez, estabele relações entre as coleções, que podem ser buscadas ao fazer as transações. Dessa forma, para garantir as cardinalidades entre as coleções algumas propriedades devem ser elaboradas. Inicialmente as coleções precisam conter chaves estrangeiras (do inglês, Foreing Key - FK), para fazer o relacionamento entre sí. A coleção Carro para preservar a cardinalidade 0..\*:1 (nenhum ou muitos para um) deve conter uma FK para a coleção Modelo. Assim como a coleção Modelo deve conter uma FK para a coleção Marca, mantendo a mesma cardinalidade 0..\*:1.

Ainda sobre as FK, é preciso garantir que ela não seja um array, e seja um valor único de referência na tabela especificada. Caso contrário, as relações de cardinalidade não serão garantidas. 

## Como executar

Para executar o projeto, basta baixar o mongoDB, iniciar uma conexão com ele.

baixar as dependências: 
pip install Flask
pip install pymongo

Executar o script "criar_banco.py" e após isso o script "app.py". 

Com a api rodando, basta utilizar os endpoints fornecidos, em algum software como postman. 
