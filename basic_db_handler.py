"""
Это супер-базовый пример,
так делать нельзя

поставить psycopg2 командой

uv add psycopg2-binary

"""

import psycopg2

# Данные для примера
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="test_db",
    user="test_user",
    password="test"  # В реальности так делать нельзя, об этом мы поговорим,
    # когда будем использовать переменные окружения
)

cur = conn.cursor()

# Example SELECT
query = "SELECT id FROM test_users WHERE id < %s"
cur.execute(query, (25,))
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
