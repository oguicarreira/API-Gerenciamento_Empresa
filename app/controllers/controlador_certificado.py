from flask import Blueprint, request, jsonify, current_app
from app.usecases.servico_certificado import ServicoCertificado
from app.usecases.servico_notificacao import ServicoNotificacao

bp_certificado = Blueprint('bp_certificado', __name__)

def inicializaServicoNotificacao():
    if 'servico_notificacao' not in current_app.extensions:
        current_app.extensions['servico_notificacao'] = ServicoNotificacao(current_app)
    return current_app.extensions['servico_notificacao']

@bp_certificado.route('/certificado', methods=['POST'])
def createCertificado():
    requisicao = request.json
    ServicoCertificado.createCertificado(requisicao)
    return jsonify({'message': 'Certificado criado com sucesso!'}), 201

@bp_certificado.route('/certificado/<int:id>', methods=['GET'])
def readCertificadoPeloId(id):
    certificado = ServicoCertificado.readCertificadoPeloId(id)
    if certificado:
        return jsonify(certificado.__dict__)
    return jsonify({'message': 'Certificado não encontrado!'}), 404

@bp_certificado.route('/certificado', methods=['GET'])
def readCertificado():
    certificados = ServicoCertificado.readCertificado()
    return jsonify([certificado.__dict__ for certificado in certificados])

@bp_certificado.route('/certificado/<int:id>', methods=['PUT'])
def updateCertificado(id):
    requisicao = request.json
    update = ServicoCertificado.updateCertificado(id, requisicao)
    if update:
        return jsonify({'message': 'Certificado atualizado com sucesso!'})
    return jsonify({'message': 'Certificado não encontrado!'}), 404

@bp_certificado.route('/certificado/<int:id>', methods=['DELETE'])
def deleteCertificado(id):
    delete = ServicoCertificado.deleteCertificado(id)
    if delete:
        return jsonify({'message': 'Certificado deletado com sucesso!'})
    return jsonify({'message': 'Certificado não encontrado!'}), 404

@bp_certificado.route('/notificacertificado/<int:id>', methods=['GET', 'POST'])
def notificaCertificado(id):
    servico_notificacao = inicializaServicoNotificacao()
    notifica = servico_notificacao.notificaCertificado(id)
    if notifica:
        return jsonify({'message': 'Email enviado com sucesso!!'})
    return jsonify({'message': 'O certificado não está próximo de expirar!!'}), 404