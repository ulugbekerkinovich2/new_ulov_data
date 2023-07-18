import pandas as pd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auto_ru.settings')
# django.setup()

from django.db import connection

df = pd.read_excel('vehicle_data (2)_yangi.xlsx', sheet_name='Sheet 1')
data = df.values
for i in range(len(data)):
    row = data[i]
    mark = str(row[1]).lower().capitalize()
    model = str(row[2]).lower().capitalize()
    body = str(row[3]).lower().capitalize()
    fuel = str(row[4]).lower().capitalize()

    # Execute SQL query to insert data into the database
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO vehicle (mark_name, model_name, body, fuel) VALUES (%s, %s, %s, %s)",
            [mark, model, body, fuel]
        )
