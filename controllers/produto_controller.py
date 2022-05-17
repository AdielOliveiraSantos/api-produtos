from flask import Blueprint, request, make_response, jsonify

from app import db
from app.models.produto import Produto
from app.models.produto_schema import ProdutoSchema


class ProdutoController:

    produto_controller = Blueprint(name='produto_controller', import_name=__name__)

    @produto_controller.route('/produto', methods=['GET'])
    def index():
        lista_de_produtos = Produto.query.all()
        produto_schema = ProdutoSchema(many=True)
        produtos = produto_schema.dump(lista_de_produtos)


        return make_response(jsonify({
            "produtos" : produtos
        }))

    @produto_controller.route('/produtos/<id>', methods=['Get'])
    def get_produto(id):
        produto = Produto.query.get(id)
        produto_schema = ProdutoSchema()
        produtos = produto_schema.dump(produto)

        return make_response(jsonify({
            "produtos" : produtos
        }))

    @produto_controller.route('/produtos', methods=['POST'])
    def create():
        dados = request.get.json()

        produto_schema = ProdutoSchema()
        produto = produto_schema.load(dados)

        resultado = produto_schema.dump(produto.create())

        return make_response(jsonify({
            "produtos" : resultado
        }), 201)


    @produto_controller.route('/produto/<id>', methods=['DELETE'])
    def delete(id):

        produto = Produto.query.get(id)
        db.seassion.delete(produto)
        db.seassion.conmit()
        return make_response(jsonify({}), 204)

    @produto_controller.route('/produtos/<id>', methods=['PUT'])
    def update(id):

        produto = Produto.query.get(id)
        dados = request.get.json().get('produtos')
        produto_schema = ProdutoSchema()

        if dados.get('nome'):
            produto.nome = dados['nome']

        if dados.get('preco'):
            produto.nome = dados['preco']

        if dados.get('quantidade'):
            produto.nome = dados['quantidade']

        db.seassion.add(produto)
        db.seassion.commit()

        produto_atualizado = produto_schema.dump(produto)

        return make_response(jsonify({
            "produtos" : produto_atualizado
        }), 200)



