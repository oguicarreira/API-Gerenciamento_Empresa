#bibliotecas
from flask import Flask, make_response, jsonify, request
from flask_mail import Mail, Message
from connect import dbpost
from config import email, senha
from datetime import datetime

#verifica se o BD está conectado corretamente
print(dbpost.info)

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.secret_key = 'teste'

#Configurações do Gmail para notificação por e-mail
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail = Mail(app)

#ReadRouts
@app.route('/funcionario', methods=['GET'])
def readFuncionario():
    cursor = dbpost.cursor()
    cursor.execute(f'SELECT * FROM funcionario')
    fun = cursor.fetchall()

    return make_response(
        jsonify(
            dados=fun
        )
    )

@app.route('/veiculo', methods=['GET'])
def readVeiculo():
    cursor = dbpost.cursor()
    cursor.execute(f'SELECT * FROM veiculo')
    vei = cursor.fetchall()

    return make_response(
        jsonify(
            dados=vei
        )
    )

@app.route('/estoque_ativo', methods=['GET'])
def readEstoqueAtivo():
    cursor = dbpost.cursor()
    cursor.execute(f'SELECT * FROM estoque_ativo')
    esta = cursor.fetchall()

    return make_response(
        jsonify(
            dados=esta
        )
    )

@app.route('/estoque_passivo', methods=['GET'])
def readEstoquePassivo():
    cursor = dbpost.cursor()
    cursor.execute(f'SELECT * FROM estoque_passivo')
    estp = cursor.fetchall()

    return make_response(
        jsonify(
            dados=estp
        )
    )

@app.route('/certificado', methods=['GET'])
def readCertificado():
    cursor = dbpost.cursor()
    cursor.execute(f'SELECT f.nome, c.descricao, c.data_expiracao FROM certificado c INNER JOIN funcionario f ON c.id_funcionario = f.id')
    cer = cursor.fetchall()
    return make_response(
        jsonify(
            dados=cer
        )
    )

#notifica quando certificado está próximo de expirar
@app.route('/notifica/certificado/<id>', methods=['GET', 'POST'])
def notificaCertificado(id):
    cursor = dbpost.cursor()
    cursor.execute(f'SELECT data_expiracao FROM certificado WHERE id_funcionario = {id}')
    c = cursor.fetchone()
    if c:
        data = c[0]
        hoje = datetime.now().date()
        diferenca = data - hoje
    if diferenca.days < 30:
        msg = Message(
            subject = 'Aviso de Expiração de Certificado!',
            sender = app.config.get("MAIL_USERNAME"),
            recipients = [app.config.get("MAIL_USERNAME")],
            body = f'''
            Seu certificado expira em menos de 30 dias!

            '''
        )
        mail.send(msg)
        return make_response(
            jsonify(
                mensagem='Email enviado com sucesso!',
            )
        )
    else:
        return make_response(
            jsonify(
                mensagem='O certificado não está próximo de expirar!',
            )
        )

#Rota para baixas no estoque ativo
@app.route('/baixa_estoque_ativo', methods=['POST', 'GET'])
def baixaEstoqueativo():
    ins = request.json
    cursor = dbpost.cursor()
    sql = f"INSERT INTO emprestimos_estoque_ativo (id_funcionario, id_estoque_ativo) VALUES ('{ins['id_funcionario']}', '{ins['id_estoque_ativo']}') ON CONFLICT (id_estoque_ativo) DO NOTHING"
    select = f"SELECT f.nome, ea.nome FROM emprestimos_estoque_ativo INNER JOIN funcionario f ON id_funcionario = f.id INNER JOIN estoque_ativo ea ON id_estoque_ativo = ea.id"
    cursor.execute(sql)
    dbpost.commit()
    cursor.execute(select)
    sel = cursor.fetchall()

    return make_response(
        jsonify(
            dados=sel
        )
    )

#DELETEs
@app.route('/delete_emprestimo/<id>', methods=['DELETE'])
def deleteEmprestimo(id):
    cursor = dbpost.cursor()
    sql = f"DELETE FROM emprestimos_estoque_ativo WHERE id_estoque_ativo = {id}"
    cursor.execute(sql)
    dbpost.commit()

    return make_response(
        jsonify(
            Message='Empréstimo deletado com sucesso!'
        )
    )

@app.route('/delete_estoque_passivo/<id>', methods=['DELETE'])
def deleteEstoquePassivo(id):
    cursor = dbpost.cursor()
    sql = f"DELETE FROM estoque_passivo WHERE id = {id}"
    cursor.execute(sql)
    dbpost.commit()

    return make_response(
        jsonify(
            Message='Item deletado com sucesso!'
        )
    )

if __name__ == '__main__':
    app.run(debug=True)