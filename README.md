# Gerenciamento_Empresa
API de gestão de empresa (estoques, funcionário, veículos, certificados) usando Python, Flask e PostgreSQL em Clean Archtecture

## Preparando o ambiente virtual
Criar a pasta do projeto, colar o arquivo 'main.py' e abrir no seu editor de código;
Executar os seguintes comandos no terminal:
cd <caminho_da_pasta_do_projeto>
py -m venv venv
venv\Scripts\activate

## Instalando bibliotecas
No terminal realizar os seguintes comandos:
pip install Flask 
pip install psycopg2
pip install Flask-Mail

## Criando o arquivo para configuração do banco de dados e do email e senha para notificação
Na pasta do projeto, criar o arquivo 'config.py' e colocas as seguintes váriaveis:
userdb = '<nome_de_usuario_BD>'
senhadb = '<senha_BD>'
email = '<email>'
senha = '<senha>'
