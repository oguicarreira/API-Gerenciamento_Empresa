from flask import Blueprint, request, jsonify
from app.usecases.servico_funcionario import ServicoFuncionario

bp_funcionario = Blueprint('bp_funcionario', __name__)

@bp_funcionario.route('/funcionario', methods=['POST'])
def createFuncionario():
    requisicao = request.json
    ServicoFuncionario.createFuncionario(requisicao)
    return jsonify({'message': 'Funcionário criado com sucesso!'}), 201

@bp_funcionario.route('/funcionario/<int:id>', methods=['GET'])
def readFuncionarioPeloId(id):
    funcionario = ServicoFuncionario.readFuncionarioPeloId(id)
    if funcionario:
        return jsonify(funcionario.__dict__)
    return jsonify({'message': 'Funcionário não encontrado!'}), 404

@bp_funcionario.route('/funcionario', methods=['GET'])
def readFuncionario():
    funcionarios = ServicoFuncionario.readFuncionario()
    return jsonify([funcionario.__dict__ for funcionario in funcionarios])

@bp_funcionario.route('/funcionario/<int:id>', methods=['PUT'])
def updateFuncionario(id):
    requisicao = request.json
    update = ServicoFuncionario.updateFuncionario(id, requisicao)
    if update:
        return jsonify({'message': 'Funcionário atualizado com sucesso!'})
    return jsonify({'message': 'Funcionário não encontrado!'}), 404

@bp_funcionario.route('/funcionario/<int:id>', methods=['DELETE'])
def deleteFuncionario(id):
    delete = ServicoFuncionario.deleteFuncionario(id)
    if delete:
        return jsonify({'message': 'Funcionário deletado com sucesso!'})
    return jsonify({'message': 'Funcionario não encontrado!'}), 404
