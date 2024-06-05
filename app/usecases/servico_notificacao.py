from flask_mail import Mail, Message
from config import email, senha
from connect import dbpost
from datetime import datetime

class ServicoNotificacao:
    def __init__(self, app):
        self.app = app
        self.mail_settings = {
            "MAIL_SERVER": 'smtp.gmail.com',
            "MAIL_PORT": 465,
            "MAIL_USE_TLS": False,
            "MAIL_USE_SSL": True,
            "MAIL_USERNAME": email,
            "MAIL_PASSWORD": senha
        }
        self.mail = Mail(self.app)
        self.app.config.update(self.mail_settings)

    def notificaCertificado(self, id_certificado):
        cursor = dbpost.cursor()
        cursor.execute('SELECT data_expiracao FROM certificado WHERE id_funcionario = %s', (id_certificado,))
        c = cursor.fetchone()
        if c:
            data = c[0]
            hoje = datetime.now().date()
            diferenca = data - hoje
            if diferenca.days < 30:
                msg = Message(
                    subject='Aviso de Expiração de Certificado!',
                    sender=self.app.config.get("MAIL_USERNAME"),
                    recipients=[self.app.config.get("MAIL_USERNAME")],
                    body=f'Seu certificado expira em menos de 30 dias!'
                )
                self.mail.send(msg)
                return True
        return False
