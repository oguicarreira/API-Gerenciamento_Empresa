from flask import Blueprint, request, jsonify
from app.usecases.servico_cargo import ServicoCargo

bp_cargo = Blueprint('bp_cargo', __name__)

@bp_cargo.route('/cargo', methods=['POST'])
def createCargo():
    requisicao = request.json
    ServicoCargo.createCargo(requisicao)
    return jsonify({'message': 'Cargo criado com sucesso!'}), 201

@bp_cargo.route('/cargo/<int:id>', methods=['GET'])
def readCargoPeloId(id):
    cargo = ServicoCargo.readCargoPeloId(id)
    if cargo:
        return jsonify(cargo.__dict__)
    return jsonify({'message': 'Cargo não encontrado!'}), 404

@bp_cargo.route('/cargo', methods=['GET'])
def readCargo():
    cargos = ServicoCargo.readCargo()
    return jsonify([cargo.__dict__ for cargo in cargos])

@bp_cargo.route('/cargo/<int:id>', methods=['PUT'])
def updateCargo(id):
    requisicao = request.json
    update = ServicoCargo.updateCargo(id, requisicao)
    if update:
        return jsonify({'message': 'Cargo atualizado com sucesso!'})
    return jsonify({'message': 'Cargo não encontrado!'}), 404

@bp_cargo.route('/cargo/<int:id>', methods=['DELETE'])
def deleteCargo(id):
    delete = ServicoCargo.deleteCargo(id)
    if delete:
        return jsonify({'message': 'Cargo deletado com sucesso!'})
    return jsonify({'message': 'Cargo não encontrado!'}), 404
