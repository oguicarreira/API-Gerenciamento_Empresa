from app.entities.estoque_passivo import EstoquePassivo
from connect import dbpost

class ServicoEstoquePassivo:

    @staticmethod
    def readEstoquePassivo():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM estoque_passivo')
        estoquepassivos = cursor.fetchall()
        return [EstoquePassivo(*estoquepassivo) for estoquepassivo in estoquepassivos]

    @staticmethod
    def readEstoquePassivoPeloId(id_estoque_passivo):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM estoque_passivo WHERE id = %s', (id_estoque_passivo,))
        estoquepassivo = cursor.fetchone()
        if estoquepassivo:
            return EstoquePassivo(*estoquepassivo)
        return None

    @staticmethod
    def createEstoquePassivo(info_estoque_passivo):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO estoque_passivo (nome, descricao, preco, quantidade)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(sql, (
            info_estoque_passivo['nome'],
            info_estoque_passivo['descricao'],
            info_estoque_passivo['preco'],
            info_estoque_passivo['quantidade']
        ))
        dbpost.commit()

    @staticmethod
    def updateEstoquePassivo(id_estoque_passivo, info_estoque_passivo):
        cursor = dbpost.cursor()
        sql = '''
            UPDATE estoque_passivo
            SET nome = %s, descricao = %s, preco = %s, quantidade = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (
            info_estoque_passivo['nome'],
            info_estoque_passivo['descricao'],
            info_estoque_passivo['preco'],
            info_estoque_passivo['quantidade'],
            id_estoque_passivo
        ))
        dbpost.commit()
        return cursor.rowcount > 0

    @staticmethod
    def deleteEstoquePassivo(id_estoque_passivo):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM estoque_passivo WHERE id = %s', (id_estoque_passivo,))
        dbpost.commit()
        return cursor.rowcount > 0