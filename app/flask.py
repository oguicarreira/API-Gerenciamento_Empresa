from flask import Flask
from app.controllers import registroBP

def funcaoInicializa():
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False
    app.secret_key = 'teste'
    registroBP(app)

    return app
