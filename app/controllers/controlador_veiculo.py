from flask import Blueprint, request, jsonify
from app.usecases.servico_veiculo import ServicoVeiculo

bp_veiculo = Blueprint('bp_veiculo', __name__)

@bp_veiculo.route('/veiculo', methods=['POST'])
def createVeiculo():
    requisicao = request.json
    ServicoVeiculo.createVeiculo(requisicao)
    return jsonify({'message': 'Veículo criado com sucesso!'}), 201

@bp_veiculo.route('/veiculo/<int:id>', methods=['GET'])
def readVeiculoPeloId(id):
    veiculo = ServicoVeiculo.readVeiculoPeloId(id)
    if veiculo:
        return jsonify(veiculo.__dict__)
    return jsonify({'message': 'Veículo não encontrado!'}), 404

@bp_veiculo.route('/veiculo', methods=['GET'])
def readVeiculo():
    veiculos = ServicoVeiculo.readVeiculo()
    return jsonify([veiculo.__dict__ for veiculo in veiculos])

@bp_veiculo.route('/veiculo/<int:id>', methods=['PUT'])
def updateVeiculo(id):
    requisicao = request.json
    update = ServicoVeiculo.updateVeiculo(id, requisicao)
    if update:
        return jsonify({'message': 'Veículo atualizado com sucesso!'})
    return jsonify({'message': 'Veículo não encontrado!'}), 404

@bp_veiculo.route('/veículo/<int:id>', methods=['DELETE'])
def deleteVeiculo(id):
    delete = ServicoVeiculo.deleteVeiculo(id)
    if delete:
        return jsonify({'message': 'Veículo deletado com sucesso!'})
    return jsonify({'message': 'Veículo não encontrado!'}), 404
