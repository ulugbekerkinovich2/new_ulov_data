import psycopg2
import pyaspeller

connect = psycopg2.connect(
    dbname="car_com2",
    user="postgres",
    password="0852",
    host="127.0.0.1",
    port="5432"
)
cursor = connect.cursor()
cursor.execute("SELECT * FROM mark")
row = cursor.fetchall()
speller = pyaspeller.YandexSpeller(lang=['ru', 'en'])

for i in row:
    print(i)
    row_id = i[0]
    row_name = i[1]
    corrected_word = speller.spelled(row_name)
    print(row_name)
    print(corrected_word + '\n\n')
    cursor.execute("UPDATE mark SET mark_name=%s WHERE id=%s", (row_name, row_id))
    connect.commit()

cursor.execute("SELECT * FROM model1")
row1 = cursor.fetchall()
speller = pyaspeller.YandexSpeller(lang=['ru', 'en'])
for i in row1:
    print(i)
    row1_id = i[0]
    row1_model_name = i[1]
    row1_mark_id = i[2]
    # print(row1_id, row1_model_name, row1_mark_id)
    corrected_wrod1 = speller.spelled(row1_model_name)
    print(row1_model_name)
    print(corrected_wrod1 + '\n\n')
    cursor.execute('UPDATE model1 SET model_name=%s WHERE id=%s', (row1_model_name, row1_id))
    connect.commit()
