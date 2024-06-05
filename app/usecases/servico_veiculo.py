from app.entities.veiculo import Veiculo
from connect import dbpost

class ServicoVeiculo:

    @staticmethod
    def readVeiculo():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM veiculo')
        veiculos = cursor.fetchall()
        return [Veiculo(*veiculo) for veiculo in veiculos]

    @staticmethod
    def readVeiculoPeloId(id_veiculo):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM veiculo WHERE id = %s', (id_veiculo,))
        veiculo = cursor.fetchone()
        if veiculo:
            return Veiculo(*veiculo)
        return None

    @staticmethod
    def createVeiculo(info_veiculo):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO veiculo (modelo, ano, categoria, marca)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(sql, (
            info_veiculo['modelo'],
            info_veiculo['ano'],
            info_veiculo['categoria'],
            info_veiculo['marca']
        ))
        dbpost.commit()

    @staticmethod
    def updateVeiculo(id_veiculo, info_veiculo):
        cursor = dbpost.cursor()
        sql = '''
            UPDATE veiculo
            SET modelo = %s, ano = %s, categoria = %s, marca = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (
            info_veiculo['modelo'],
            info_veiculo['ano'],
            info_veiculo['categoria'],
            info_veiculo['marca'],
            id_veiculo
        ))
        dbpost.commit()
        return cursor.rowcount > 0

    @staticmethod
    def deleteVeiculo(id_veiculo):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM veiculo WHERE id = %s', (id_veiculo,))
        dbpost.commit()
        return cursor.rowcount > 0