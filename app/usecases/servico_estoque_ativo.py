from app.entities.estoque_ativo import EstoqueAtivo
from connect import dbpost

class ServicoEstoqueAtivo:

    @staticmethod
    def readEstoqueAtivo():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM estoque_ativo')
        estoqueativos = cursor.fetchall()
        return [EstoqueAtivo(*estoqueativo) for estoqueativo in estoqueativos]

    @staticmethod
    def readEstoqueAtivoPeloId(id_estoque_ativo):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM estoque_ativo WHERE id = %s', (id_estoque_ativo,))
        estoqueativo = cursor.fetchone()
        if estoqueativo:
            return EstoqueAtivo(*estoqueativo)
        return None

    @staticmethod
    def createEstoqueAtivo(info_estoque_ativo):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO estoque_ativo (nome)
            VALUES (%s)
        '''
        cursor.execute(sql, (
            info_estoque_ativo['nome']
        ))
        dbpost.commit()

    @staticmethod
    def updateEstoqueAtivo(id_estoque_ativo, info_estoque_ativo):
        cursor = dbpost.cursor()
        sql = '''
            UPDATE estoque_ativo
            SET nome = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (
            info_estoque_ativo['nome'],
            id_estoque_ativo
        ))
        dbpost.commit()
        return cursor.rowcount > 0

    @staticmethod
    def deleteEstoqueAtivo(id_estoque_ativo):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM estoque_ativo WHERE id = %s', (id_estoque_ativo,))
        dbpost.commit()
        return cursor.rowcount > 0