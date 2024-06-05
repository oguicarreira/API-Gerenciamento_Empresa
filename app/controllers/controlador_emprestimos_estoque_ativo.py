from flask import Blueprint, request, jsonify
from app.usecases.servico_emprestimos_estoque_ativo import ServicoEmprestimosEstoqueAtivo

bp_emprestimos_estoque_ativo = Blueprint('bp_emprestimos_estoque_ativo', __name__)

@bp_emprestimos_estoque_ativo.route('/emprestimosestoqueativo', methods=['POST'])
def createEmprestimosEstoqueAtivo():
    requisicao = request.json
    ServicoEmprestimosEstoqueAtivo.createEmprestimosEstoqueAtivo(requisicao)
    return jsonify({'message': 'Empréstimo criado com sucesso!'}), 201

@bp_emprestimos_estoque_ativo.route('/emprestimosestoqueativo/<int:id>', methods=['GET'])
def readEmprestimosEstoqueAtivoPeloId(id):
    emprestimo = ServicoEmprestimosEstoqueAtivo.readEmprestimosEstoqueAtivoPeloId(id)
    if emprestimo:
        return jsonify(emprestimo.__dict__)
    return jsonify({'message': 'Empréstimo não encontrado!'}), 404

@bp_emprestimos_estoque_ativo.route('/emprestimosestoqueativo', methods=['GET'])
def readEmprestimosEstoqueAtivo():
    emprestimos = ServicoEmprestimosEstoqueAtivo.readEmprestimosEstoqueAtivo()
    return jsonify([emprestimo.__dict__ for emprestimo in emprestimos])

@bp_emprestimos_estoque_ativo.route('/emprestimosestoqueativo/<int:id>', methods=['DELETE'])
def deleteEmprestimosEstoqueAtivo(id):
    delete = ServicoEmprestimosEstoqueAtivo.deleteEmprestimosEstoqueAtivo(id)
    if delete:
        return jsonify({'message': 'Empréstimos deletado com sucesso!'})
    return jsonify({'message': 'Empréstimos não encontrado!'}), 404
