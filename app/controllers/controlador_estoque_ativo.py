from flask import Blueprint, request, jsonify
from app.usecases.servico_estoque_ativo import ServicoEstoqueAtivo

bp_estoque_ativo = Blueprint('bp_estoque_ativo', __name__)

@bp_estoque_ativo.route('/estoqueativo', methods=['POST'])
def createEstoqueAtivo():
    requisicao = request.json
    ServicoEstoqueAtivo.createEstoqueAtivo(requisicao)
    return jsonify({'message': 'Estoque criado com sucesso!'}), 201

@bp_estoque_ativo.route('/estoqueativo/<int:id>', methods=['GET'])
def readEstoqueAtivoPeloId(id):
    estoque = ServicoEstoqueAtivo.readEstoqueAtivoPeloId(id)
    if estoque:
        return jsonify(estoque.__dict__)
    return jsonify({'message': 'Estoque não encontrado!'}), 404

@bp_estoque_ativo.route('/estoqueativo', methods=['GET'])
def readEstoqueAtivo():
    estoques = ServicoEstoqueAtivo.readEstoqueAtivo()
    return jsonify([estoque.__dict__ for estoque in estoques])

@bp_estoque_ativo.route('/estoqueativo/<int:id>', methods=['PUT'])
def updateEstoqueAtivo(id):
    requisicao = request.json
    update = ServicoEstoqueAtivo.updateEstoqueAtivo(id, requisicao)
    if update:
        return jsonify({'message': 'Estoque atualizado com sucesso!'})
    return jsonify({'message': 'Estoque não encontrado!'}), 404

@bp_estoque_ativo.route('/estoqueativo/<int:id>', methods=['DELETE'])
def deleteEstoqueAtivo(id):
    delete = ServicoEstoqueAtivo.deleteEstoqueAtivo(id)
    if delete:
        return jsonify({'message': 'Estoque deletado com sucesso!'})
    return jsonify({'message': 'Estoque não encontrado!'}), 404
