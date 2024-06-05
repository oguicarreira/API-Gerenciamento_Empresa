from app.entities.funcionario import Funcionario
from connect import dbpost

class ServicoFuncionario:

    @staticmethod
    def readFuncionario():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM funcionario')
        funcionarios = cursor.fetchall()
        return [Funcionario(*funcionario) for funcionario in funcionarios]

    @staticmethod
    def readFuncionarioPeloId(id_funcionario):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM funcionario WHERE id = %s', (id_funcionario,))
        funcionario = cursor.fetchone()
        if funcionario:
            return Funcionario(*funcionario)
        return None

    @staticmethod
    def createFuncionario(info_funcionario):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO funcionario (nome, cpf, data_nasc, cidade, estado, endereco, celular, categoria_cnh)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (
            info_funcionario['nome'],
            info_funcionario['cpf'],
            info_funcionario['data_nasc'],
            info_funcionario['cidade'],
            info_funcionario['estado'],
            info_funcionario['endereco'],
            info_funcionario['celular'],
            info_funcionario['categoria_cnh']
        ))
        dbpost.commit()

    @staticmethod
    def updateFuncionario(id_funcionario, info_funcionario):
        cursor = dbpost.cursor()
        sql = '''
            UPDATE funcionario
            SET nome = %s, cpf = %s, data_nasc = %s, cidade = %s, estado = %s, endereco = %s, celular = %s, categoria_cnh = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (
            info_funcionario['nome'],
            info_funcionario['cpf'],
            info_funcionario['data_nasc'],
            info_funcionario['cidade'],
            info_funcionario['estado'],
            info_funcionario['endereco'],
            info_funcionario['celular'],
            info_funcionario['categoria_cnh'],
            id_funcionario
        ))
        dbpost.commit()
        return cursor.rowcount > 0

    @staticmethod
    def deleteFuncionario(id_funcionario):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM funcionario WHERE id = %s', (id_funcionario,))
        dbpost.commit()
        return cursor.rowcount > 0