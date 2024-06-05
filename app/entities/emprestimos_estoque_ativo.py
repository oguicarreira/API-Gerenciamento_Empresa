class EmprestimosEstoqueAtivo:
    def __init__(self, id_funcionario, id_estoque_ativo):
        self.id_funcionario = id_funcionario
        self.id_estoque_ativo = id_estoque_ativo

    def __repr__(self):
        return f"<EmprestimoEstoqueAtivo Funcionario ID: {self.id_funcionario}, EstoqueAtivo ID: {self.id_estoque_ativo}>"