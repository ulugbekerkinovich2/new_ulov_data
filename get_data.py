import difflib
import time
import pyexcelerate as px
import pandas as pd
import psycopg2
import requests
import xlwt
import openpyxl
from openpyxl.utils import get_column_letter
import xlrd

connect = psycopg2.connect(
    dbname="car_com2",
    user="postgres",
    password="0852",
    host="127.0.0.1",
    port="5432")


# from django.db import connections
# connect = connections
def split_by2(text):
    split_by_2 = []
    joined_data = []
    words = text.split(" ")
    for i in range(0, len(words), 2):
        if i + 1 < len(words):
            split_by_2.append(words[i] + " " + words[i + 1])
        else:
            split_by_2.append(words[i])
    for k in split_by_2:
        joined_data.append(k)
    print("Split by every second space:", joined_data)
    return joined_data


# def max_string(strings):
#     max_length = 0
#     max_string = ""
#     for s in strings:
#         if len(s) > max_length:
#             max_length = len(s)
#             max_string = s
#     return max_string


# Split by every third space
def split_by3(text):
    split_by_3 = [text.split(" ")[i:i + 3] for i in range(0, len(text.split(" ")), 3)]
    joined_data = []
    for j in split_by_3:
        joined_data.append(j)
    print("Split by every third space:", joined_data)
    return joined_data


def remove_symbols(text, symbols):
    for symbol in symbols:
        text = text.replace(symbol, ' ')
        text = text.replace('  ', ' ')
    return text


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAFeaNW1dtleNNM4DDPBnvpC7XdtTZ687mo/"
            f"sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


def details(file_name):
    telebots('write to excell file')
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    connect.autocommit = True
    cursor = connect.cursor()
    cursor.execute("SELECT model_name FROM model1")
    cars_model = cursor.fetchall()
    # print(cars_model)
    # time.sleep(500)
    list_of_cars_model = []
    for car in cars_model:
        car_model = ' '.join(map(str, car[0].split(' ')))
        if car_model not in list_of_cars_model and type(cars_model) != int:
            list_of_cars_model.append(car_model)
    # print(list_of_cars_model)
    # time.sleep(555)
    cursor.execute("SELECT mark_name FROM mark")
    cars_mark = cursor.fetchall()
    list_of_cars_mark = []
    for car in cars_mark:
        car_mark = car[0]
        if car_mark not in list_of_cars_mark:
            list_of_cars_mark.append(car_mark)

    list_body = []
    cursor.execute("SELECT body_of_vehicle FROM body")
    body = cursor.fetchall()
    for bodys in body:
        body_ = bodys[0]
        list_body.append(body_)

    list_of_fuels = []
    cursor.execute("SELECT * FROM fuel1")
    fuels = cursor.fetchall()
    for fuel in range(len(fuels)):
        try:
            list_of_fuels.append(fuels[fuel][1])
        except Exception as e:
            print('yakunlandi barchasi qo\'shildi', e)
    cursor.execute(f"SELECT description FROM {file_name}")
    excel_data = cursor.fetchall()
    data = [i[0].lower() for i in excel_data]
    # print(data)
    data = list(set(data))
    sheet1.write(0, 0, 'Наим. Товара')
    sheet1.write(0, 1, 'Марка')
    sheet1.write(0, 2, 'Модель')
    sheet1.write(0, 3, 'Тип кузова')
    sheet1.write(0, 4, 'Тип топливо')
    count = 1
    style = xlwt.easyxf('align: wrap yes')

    # style = xlwt.easyxf('align: vertical bottom, wrap: 1')

    # def split_by1(text):
    #     split_by_1 = text.split(" ")
    #     print("Split by every space:", split_by_1)
    #     return split_by_1

    for i in data:
        try:
            sheet1.write(count, 0, f'{i}', style)
        except Exception as e:
            print(e)
            # continue
        print('\n')
        print(count)
        belgi = [',', '(', ')', '-', '+', '=', '#', '"', '"', '.', ':', ';', "'", "'", '"', ",", '/', '"\"', '.,']

        # print(remove_symbols(i, belgi))
        origin = remove_symbols(i, belgi).split(' ')

        i = ' '.join(map(str, origin))
        print(i, '\n')
        finded_mark = []
        for mark in list_of_cars_mark:
            if mark == 'man' and 'chacman' in i:
                continue
            matches = difflib.get_close_matches(mark, origin)
            if matches:
                finded_mark.append(matches[0])
            elif mark in [m for m in origin]:
                finded_mark.append(mark)
            else:
                continue
        if len(finded_mark) == 0:
            print('car_mark topilmadi')
            continue
        finded_model = []
        for model in list_of_cars_model:
            if len(model) < 3:
                continue
            if model.isnumeric() and int(model) < 100:
                continue
            if model.lower() in i:
                print(model.lower())
                finded_model.append(model)
                # print("model", model)
                finded_model = finded_model[0].replace('"', '')
                print("\033[36m" + "car_model: " f'------ {finded_model}' + "\033[0m\n")
                sheet1.write(count, 2, f'{finded_model}', style)
                break
        for mark in list_of_cars_mark:

            if mark.lower() in i:
                # print(mark)
                print("\033[36m" + "car_mark: " f'------ {mark}' + "\033[0m\n")
                sheet1.write(count, 1, f'{mark}', style)
                break
            if mark.lower() not in i:
                if finded_model:
                    # print(finded_model)
                    cursor.execute(
                        f"SELECT mark.mark_name "
                        f"FROM model1 LEFT JOIN mark ON mark.id = model1.mark_name_id "
                        f"WHERE model1.model_name =%s",
                        (finded_model,))
                    try:
                        row = cursor.fetchone()
                        print("\033[36m" + "car_mark: " f'------ {row[0]}' + "\033[0m\n")
                        sheet1.write(count, 1, f'{row[0]}', style)
                        break
                    except Exception as e:
                        print(e)
                        continue
        for fuel in list_of_fuels:
            if fuel.lower() in i.lower():
                print("\033[36m" + "car_fuel: " f'------ {fuel}' + "\033[0m\n")
                sheet1.write(count, 4, f'{fuel}', style)
                break
        for body in list_body:
            if body.lower().strip() in i.lower():
                print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                sheet1.write(count, 3, f'{body}', style)
                break
            elif body.lower() not in i.lower():
                if 'трактор' in i.lower():
                    body = 'Трактор'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    break
                if 'Микроавтобус'.lower() in i.lower():
                    body = 'Пассажирский (LCV)'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'Автобус'.lower() in i.lower():
                    body = 'Автобус'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'ЛЕГКОВОЙ'.lower() in i.lower() and 'автомобиль мини'.lower() in i.lower():
                    body = 'Легковой'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'легковой'.lower() in i.lower():
                    body = 'Легковой'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'Седельный тягач'.lower() or 'сед.тягач'.lower() in i.lower():
                    body = 'Грузовой (большой)'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'PICK-UP'.lower() and 'Грузовой'.lower() in i or 'PICK UP'.lower() and 'Грузовой'.lower() in i.lower():
                    body = 'Легковой PICK UP'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'AMBULANSE' or 'Скорая помощь' in i:
                    body = 'Скорая помощь (LCV)'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'грузовой рефрижератор'.lower() in i.lower():
                    body = 'Рефрижиратор (большой)'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'REFRIGERATOR'.lower() in i.lower():
                    body = 'Рефрижиратор (LCV)'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break
                elif 'грузовой'.lower() or 'грузавой'.lower() in i.lower():
                    body = 'Грузовой (LCV)'
                    print("\033[36m" + "car_body: " f'------ {body}' + "\033[0m\n")
                    sheet1.write(count, 3, f'{body}', style)
                    break

        count += 1
        # time.sleep(1.5)
    wb.save(f'{file_name}.xls')
    return f"{file_name}.xls"


# details(file_name='yangi_data')
# details(file_name='vehicle_data1')
# details(file_name='new_file')
