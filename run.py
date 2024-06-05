from app.flask import funcaoInicializa

app = funcaoInicializa()

if __name__ == '__main__':
    app.run(debug=True)
