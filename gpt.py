import psycopg2

conn = psycopg2.connect(
    dbname="car_com2",
    user="postgres",
    password="0852",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT id FROM model1 WHERE model_name ~ E'^\\d+$'")

# Fetch the rows and iterate over them to delete each one
rows_to_delete = cur.fetchall()
for row in rows_to_delete:
    cur.execute("DELETE FROM model1 WHERE id=%s", (row[0],))

conn.commit()

conn.close()
