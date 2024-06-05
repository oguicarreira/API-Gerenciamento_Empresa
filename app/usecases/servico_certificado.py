from app.entities.certificado import Certificado
from connect import dbpost

class ServicoCertificado:

    @staticmethod
    def readCertificado():
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM certificado')
        certificados = cursor.fetchall()
        return [Certificado(*certificado) for certificado in certificados]

    @staticmethod
    def readCertificadoPeloId(id_certificado):
        cursor = dbpost.cursor()
        cursor.execute('SELECT * FROM certificado WHERE id_funcionario = %s', (id_certificado,))
        certificado = cursor.fetchone()
        if certificado:
            return Certificado(*certificado)
        return None

    @staticmethod
    def createCertificado(info_certificado):
        cursor = dbpost.cursor()
        sql = '''
            INSERT INTO funcionario (descricao, data_expiracao, id_funcionario)
            VALUES (%s, %s, %s)
        '''
        cursor.execute(sql, (
            info_certificado['descricao'],
            info_certificado['data_expiracao'],
            info_certificado['id_funcionario']
        ))
        dbpost.commit()

    @staticmethod
    def updateCertificado(id_certificado, info_certificado):
        cursor = dbpost.cursor()
        sql = '''
            UPDATE certificado
            SET descricao = %s, data_expiracao = %s, id_funcionario = %s
            WHERE id = %s
        '''
        cursor.execute(sql, (
            info_certificado['descricao'],
            info_certificado['data_expiracao'],
            info_certificado['id_funcionario'],
            id_certificado
        ))
        dbpost.commit()
        return cursor.rowcount > 0

    @staticmethod
    def deleteCertificado(id_certificado):
        cursor = dbpost.cursor()
        cursor.execute('DELETE FROM certificado WHERE id_funcionario = %s', (id_certificado,))
        dbpost.commit()
        return cursor.rowcount > 0