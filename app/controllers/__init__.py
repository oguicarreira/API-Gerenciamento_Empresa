from flask import Blueprint
from app.controllers.controlador_funcionario import bp_funcionario
from app.controllers.controlador_veiculo import bp_veiculo
from app.controllers.controlador_cargo import bp_cargo
from app.controllers.controlador_certificado import bp_certificado
from app.controllers.controlador_estoque_ativo import bp_estoque_ativo
from app.controllers.controlador_estoque_passivo import bp_estoque_passivo
from app.controllers.controlador_emprestimos_estoque_ativo import bp_emprestimos_estoque_ativo

bp = [
    bp_funcionario,
    bp_veiculo,
    bp_cargo,
    bp_certificado,
    bp_estoque_ativo,
    bp_estoque_passivo,
    bp_emprestimos_estoque_ativo
]

def registroBP(app):
    for blueprint in bp:
        app.register_blueprint(blueprint, url_prefix='/api')
