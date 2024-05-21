#conexão com o PostgreSQL
import psycopg2
from config import userdb, senhadb

dbpost = psycopg2.connect(database = "estoque",
                           host = "localhost",
                           user = userdb,
                           password = senhadb,
                           port = "5432")