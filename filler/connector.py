import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="d.shenyagin",
    password="")

cur = conn.cursor()