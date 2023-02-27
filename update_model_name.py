import psycopg2

connect = psycopg2.connect(
    dbname="car_com2", user="postgres", password="0852", host="127.0.0.1",
    port="5432")

cursor = connect.cursor()

cursor.execute("SELECT model_name, id FROM model1")
row = cursor.fetchall()
print(row)
for i in range(len(row)):
    # print(i, '<-----')
    text_id = list(row[i])[-1]
    print(text_id, '<-')
    text = list(row[i])[0]
    text = text.split(' ')[:-1][0]
    print(text)
    cursor.execute("UPDATE model1 SET model_name = %s WHERE id = %s", (text, text_id))
    connect.commit()
