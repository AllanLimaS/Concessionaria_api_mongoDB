#pip install Flask
#pip install pymongo

# instalar essas paradas necessárias 
# rodar um python app.py para iniciar a api 

from flask import Flask, request, jsonify
from pymongo import MongoClient
#from bson import ObjectId  


##---------------------CONFIGS---------------------##

# sei lá que porra é essa, mas funciona
app = Flask(__name__)

# Conexão com o banco: esse é o valor padrão normalmente 
client = MongoClient('mongodb://localhost:27017/') 

# Nome do banco de dados
db = client['Concessionaria'] 

# Nome das "Tabelas"
colecao_carro = db['Carro']
colecao_marca = db['Marca']
colecao_modelo = db['Modelo']

##---------------------CONFIGS---------------------##


##-----------------------CARRO---------------------##

@app.route('/carro/add', methods=['POST'])
def carro_add():
    try:
        # puxa o body do request
        dados = request.get_json()

        # verifica se o modelo existe
        id_modelo = dados.get("id_modelo")
        resposta_modelo, status_code = modelo_get_by_id(id_modelo)
        if status_code == 404:
            return jsonify({"erro": "Id modelo nao existe"}), 404

        resultado = colecao_carro.insert_one(dados)

        return jsonify({"mensagem": "Inserido com sucesso", "id_inserido": str(resultado.inserted_id)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/carro/getAll', methods=['GET'])
def carro_get_All():
    try:
        carroLista = colecao_carro.find()

        carrosJson = []

        for carro in carroLista:
            carrosJson.append({
                "id": carro.get("id"),
                "id_modelo": carro.get("id_modelo"),
                "nome": carro.get("nome"),
                "renavam": carro.get("renavam"),
                "placa": carro.get("placa"),
                "valor": carro.get("valor"),
                "ano": carro.get("ano")
            })

        return jsonify(carrosJson)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/carro/getById/<string:carro_id>', methods=['GET'])
def carro_get_by_id(carro_id):
    try:

        carro = colecao_carro.find_one({"id": carro_id})

        if carro:
            carro_json = {
                "id": carro.get("id"),
                "id_modelo": carro.get("id_modelo"),
                "nome": carro.get("nome"),
                "renavam": carro.get("renavam"),
                "placa": carro.get("placa"),
                "valor": carro.get("valor"),
                "ano": carro.get("ano")
            }
            return jsonify(carro_json)
        else:
            return jsonify({"mensagem": "Carro não encontrado"}), 404

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/carro/editById/<string:carro_id>', methods=['PUT'])
def carro_edit_by_id(carro_id):
    try:
        carro = colecao_carro.find_one({"id": carro_id})
        
        if not carro:
            return jsonify({"mensagem": "Carro não encontrado"}), 404

        # Atualiza o registro com base no body do request
        dados_atualizados = request.get_json()
        colecao_carro.update_one({"id": carro_id}, {"$set": dados_atualizados})

        return jsonify({"mensagem": "Carro editado com sucesso"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/carro/deleteById/<string:carro_id>', methods=['DELETE'])
def carro_delete_by_id(carro_id):
    try:
        carro = colecao_carro.find_one({"id": carro_id})

        if not carro:
            return jsonify({"mensagem": "Carro não encontrado"}), 404

        colecao_carro.delete_one({"id": carro_id})

        return jsonify({"mensagem": "Carro excluído com sucesso"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

##-----------------------MODELO---------------------##
@app.route('/modelo/add', methods=['POST'])
def modelo_add():
    try:
        # puxa o body do request
        dados = request.get_json()

        # verifica se a marca existe
        id_marca = dados.get("id_marca")
        resposta_marca, status_code = marca_get_by_id(id_marca)
        if status_code == 404:
            return jsonify({"erro": "Id marca nao existe"}), 404

        resultado = colecao_modelo.insert_one(dados)

        return jsonify({"mensagem": "Inserido com sucesso", "id_inserido": str(resultado.inserted_id)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/modelo/editById/<string:modelo_id>', methods=['PUT'])
def modelo_edit_by_id(modelo_id):
    try:
        modelo = colecao_modelo.find_one({"id": modelo_id})
        
        if not modelo:
            return jsonify({"mensagem": "modelo não encontrado"}), 404

        # Atualiza o registro com base no body do request
        dados_atualizados = request.get_json()
        colecao_modelo.update_one({"id": modelo_id}, {"$set": dados_atualizados})

        return jsonify({"mensagem": "modelo editado com sucesso"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/modelo/deleteById/<string:modelo_id>', methods=['DELETE'])
def modelo_delete_by_id(modelo_id):
    try:
        modelo = colecao_modelo.find_one({"id": modelo_id})

        if not modelo:
            return jsonify({"mensagem": "modelo não encontrado"}), 404

        colecao_modelo.delete_one({"id": modelo_id})

        return jsonify({"mensagem": "modelo excluído com sucesso"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@app.route('/modelo/getAll', methods=['GET'])
def modelo_get_All():
    try:
        modeloLista = colecao_modelo.find()

        modelosJson = []

        for modelo in modeloLista:
            modelosJson.append({
                "id": modelo.get("id"),
                "id_marca": modelo.get("id_marca"),
                "nome": modelo.get("nome")
            })

        return jsonify(modelosJson)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/modelo/getById/<string:modelo_id>', methods=['GET'])
def modelo_get_by_id(modelo_id):
    try:

        modelo = colecao_modelo.find_one({"id": modelo_id})

        if modelo:
            modelo_json = {
                "id": modelo.get("id"),
                "id_marca": modelo.get("id_marca"),
                "nome": modelo.get("nome")
            }
            return jsonify(modelo_json), 200
        else:
            return jsonify({"mensagem": "modelo não encontrado"}), 404

    except Exception as e:
        return jsonify({"erro": str(e)}), 500
##-----------------------MARCA----------------------##

@app.route('/marca/add', methods=['POST'])
def marca_add():
    try:
        # puxa o body do request
        dados = request.get_json()

        resultado = colecao_marca.insert_one(dados)

        return jsonify({"mensagem": "Inserido com sucesso", "id_inserido": str(resultado.inserted_id)})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/marca/editById/<string:marca_id>', methods=['PUT'])
def marca_edit_by_id(marca_id):
    try:
        marca = colecao_marca.find_one({"id": marca_id})
        
        if not marca:
            return jsonify({"mensagem": "marca não encontrado"}), 404

        # Atualiza o registro com base no body do request
        dados_atualizados = request.get_json()
        colecao_marca.update_one({"id": marca_id}, {"$set": dados_atualizados})

        return jsonify({"mensagem": "marca editado com sucesso"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/marca/deleteById/<string:marca_id>', methods=['DELETE'])
def marca_delete_by_id(marca_id):
    try:
        marca = colecao_marca.find_one({"id": marca_id})

        if not marca:
            return jsonify({"mensagem": "marca não encontrado"}), 404

        colecao_marca.delete_one({"id": marca_id})

        return jsonify({"mensagem": "marca excluído com sucesso"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/marca/getAll', methods=['GET'])
def marca_get_All():
    try:
        marcaLista = colecao_marca.find()

        marcasJson = []

        for marca in marcaLista:
            marcasJson.append({
                "id": marca.get("id"),
                "nome": marca.get("nome")
            })

        return jsonify(marcasJson)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route('/marca/getById/<string:marca_id>', methods=['GET'])
def marca_get_by_id(marca_id):
    try:

        marca = colecao_marca.find_one({"id": marca_id})

        if marca:
            marca_json = {
                "id": marca.get("id"),
                "nome": marca.get("nome")
            }
            return jsonify(marca_json), 200
        else:
            return jsonify({"mensagem": "marca não encontrado"}), 404

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

#-----------------------------------------------------------------------------------#
if __name__ == '__main__':
    app.run(debug=True)


