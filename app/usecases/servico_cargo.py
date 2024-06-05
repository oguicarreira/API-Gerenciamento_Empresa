from app.entities.cargo import Cargo
from connect import dbpost

class ServicoCargo:

    @staticmethod
    def readCargo():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM cargo')
        cargos = cursor.fetchall()
        return [Cargo(*cargo) for cargo in cargos]

    @staticmethod
    def readCargoPeloId(id_cargo):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM cargo WHERE id_funcionario = %s', (id_cargo,))
        cargo = cursor.fetchone()
        if cargo:
            return Cargo(*cargo)
        return None

    @staticmethod
    def createCargo(info_cargo):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO funcionario (descricao, id_funcionario)
            VALUES (%s, %s)
        '''
        cursor.execute(sql, (
            info_cargo['descricao'],
            info_cargo['id_funcionario']
        ))
        dbpost.commit()

    @staticmethod
    def updateCargo(id_cargo, info_cargo):
        cursor = dbpost.cursor()
        sql = '''
            UPDATE cargo
            SET descricao = %s, id_funcionario = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (
            info_cargo['descricao'],
            info_cargo['id_funcionario'],
            id_cargo
        ))
        dbpost.commit()
        return cursor.rowcount > 0

    @staticmethod
    def deleteCargo(id_cargo):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM cargo WHERE id_funcionario = %s', (id_cargo,))
        dbpost.commit()
        return cursor.rowcount > 0