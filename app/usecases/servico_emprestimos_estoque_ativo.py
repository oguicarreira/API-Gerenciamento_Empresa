from app.entities.emprestimos_estoque_ativo import EmprestimosEstoqueAtivo
from connect import dbpost

class ServicoEmprestimosEstoqueAtivo:

    @staticmethod
    def readEmprestimosEstoqueAtivo():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM emprestimos_estoque_ativo')
        emprestimosestoqueativos = cursor.fetchall()
        return [EmprestimosEstoqueAtivo(*emprestimosestoqueativo) for emprestimosestoqueativo in emprestimosestoqueativos]

    @staticmethod
    def readEmprestimosEstoqueAtivoPeloId(id_estoque_ativo):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM emprestimos_estoque_ativo WHERE id = %s', (id_estoque_ativo,))
        emprestimosestoqueativo = cursor.fetchone()
        if emprestimosestoqueativo:
            return EmprestimosEstoqueAtivo(*emprestimosestoqueativo)
        return None

    @staticmethod
    def createEmprestimosEstoqueAtivo(info_emprestimos_estoque_ativo):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO emprestimos_estoque_ativo (id_funcionario, id_estoque_ativo)
            VALUES (%s, %s)
        '''
        cursor.execute(sql, (
            info_emprestimos_estoque_ativo['id_funcionario'],
            info_emprestimos_estoque_ativo['id_estoque_ativo']
        ))
        dbpost.commit()

    @staticmethod
    def deleteEmprestimosEstoqueAtivo(id_estoque_ativo):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM emprestimos_estoque_ativo WHERE id_estoque_ativo = %s', (id_estoque_ativo,))
        dbpost.commit()
        return cursor.rowcount > 0