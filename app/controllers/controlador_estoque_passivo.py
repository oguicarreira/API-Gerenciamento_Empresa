from flask import Blueprint, request, jsonify
from app.usecases.servico_estoque_passivo import ServicoEstoquePassivo

bp_estoque_passivo = Blueprint('bp_estoque_passivo', __name__)

@bp_estoque_passivo.route('/estoquepassivo', methods=['POST'])
def createEstoquePassivo():
    requisicao = request.json
    ServicoEstoquePassivo.createEstoquePassivo(requisicao)
    return jsonify({'message': 'Estoque criado com sucesso!'}), 201

@bp_estoque_passivo.route('/estoquepassivo/<int:id>', methods=['GET'])
def readEstoquePassivoPeloId(id):
    estoque = ServicoEstoquePassivo.readEstoquePassivoPeloId(id)
    if estoque:
        return jsonify(estoque.__dict__)
    return jsonify({'message': 'Estoque não encontrado!'}), 404

@bp_estoque_passivo.route('/estoquepassivo', methods=['GET'])
def readEstoquePassivo():
    estoques = ServicoEstoquePassivo.readEstoquePassivo()
    return jsonify([estoque.__dict__ for estoque in estoques])

@bp_estoque_passivo.route('/estoquepassivo/<int:id>', methods=['PUT'])
def updateEstoquePassivo(id):
    requisicao = request.json
    update = ServicoEstoquePassivo.updateEstoquePassivo(id, requisicao)
    if update:
        return jsonify({'message': 'Estoque atualizado com sucesso!'})
    return jsonify({'message': 'Estoque não encontrado!'}), 404

@bp_estoque_passivo.route('/estoquepassivo/<int:id>', methods=['DELETE'])
def deleteEstoquePassivo(id):
    delete = ServicoEstoquePassivo.deleteEstoquePassivo(id)
    if delete:
        return jsonify({'message': 'Estoque deletado com sucesso!'})
    return jsonify({'message': 'Estoque não encontrado!'}), 404
