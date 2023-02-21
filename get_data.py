import difflib
import re
import time
from difflib import get_close_matches

import pandas as pd
import psycopg2
import requests
import xlwt

# from write_from_excell import telebots

connect = psycopg2.connect(
    dbname="car_com2", user="postgres", password="0852", host="127.0.0.1",
    port="5432")


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAFeaNW1dtleNNM4DDPBnvpC7XdtTZ687mo/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


def details(file_name):
    telebots('write to new excell file')
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet('Sheet 2')

    connect.autocommit = True
    cursor = connect.cursor()
    cursor.execute("SELECT model_name FROM model1")
    cars_model = cursor.fetchall()
    list_of_cars_model = []
    for car in cars_model:
        car_model = ' '.join(map(str, car[0].split(' ')[:-1]))
        if car_model not in list_of_cars_model and type(cars_model) != int:
            list_of_cars_model.append(car_model)
    # print(list_of_cars_model)
    # time.sleep(555)
    cursor.execute("SELECT mark_name FROM mark")
    cars_mark = cursor.fetchall()
    list_of_cars_mark = []
    for car in cars_mark:
        car_mark = car[0]
        # print(car_mark)
        # time.sleep(550)
        if car_mark not in list_of_cars_mark:
            list_of_cars_mark.append(car_mark)
    # print(list_of_cars_mark)
    # print("model: ", cars[0][1],
    #       "mark: ", cars[0][2])
    list_of_fuels = []
    cursor.execute("SELECT * FROM fuel1")
    fuels = cursor.fetchall()
    for fuel in range(len(fuels)):
        try:
            list_of_fuels.append(fuels[fuel][1])
        except:
            print('yakunlandi barchasi qo\'shildi')
    # print('fuel: ', fuels[0][1])
    # print(list_of_fuels)

    # print('data: ', excel_data)
    # list_of_kuzov = []
    # cursor.execute("SELECT * FROM kuzov_turi")
    # kuzov = cursor.fetchall()
    # for kuz in range(1, len(kuzov) + 1):
    #     try:
    #         list_of_kuzov.append(kuzov[kuz][1])
    #     except:
    #         print('yakunlandi kuzovlar')
    list_of_excell_data = []
    cursor.execute(f"SELECT description FROM {file_name}")
    excel_data = cursor.fetchall()
    # for i in range(len(excel_data)):
    #     list_of_excell_data.append(excel_data[i])
    # print(list_of_excell_data)
    # for i in excel_data:
    #     print(i)
    #     print('\n\n')
    #     time.sleep(2)
    data = [i[0].lower() for i in excel_data]
    print(data)
    data = list(set(data))
    sheet1.write(0, 0, 'Наим. Товара')
    sheet1.write(0, 1, 'Марка')
    sheet1.write(0, 2, 'Модель')
    sheet1.write(0, 3, 'Тип кузова')
    sheet1.write(0, 4, 'Тип топливо')
    count = 1
    style = xlwt.easyxf('align: wrap yes')

    def split_by1(text):
        split_by_1 = text.split(" ")
        print("Split by every space:", split_by_1)
        return split_by_1

    def max_string(strings):
        max_length = 0
        max_string = ""
        for s in strings:
            if len(s) > max_length:
                max_length = len(s)
                max_string = s
        return max_string

    for i in data:
        print(i)
        print(count)
        sheet1.write(count, 1, f'{i.strip().lower()}', style)
        # print(i)
        print('\n')
        belgi = [',', '(', ')', '-', '+', '=', '#', '"', '"', '.', ':', ';', "'", "'", '"', ",", '/', '"\"']

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
            return text

        # print(remove_symbols(i, belgi))
        origin = remove_symbols(i, belgi)
        list_m = []
        list1_m1 = []
        # time.sleep(50)
        word_extra = []
        for m in list_of_cars_model:
            if len(m) == 1:
                split_text = split_by1(origin)
                split_text = list(dict.fromkeys(split_text))
                split_text = ' '.join(map(str, split_text))
                for el in split_text:
                    if m.lower().strip() in el.lower().strip() or m.lower().strip() == el.lower().strip():
                        list_m.append(m)
        matches = difflib.get_close_matches(list_of_cars_model, list_m)
        # maxim = max_string(list_m)
        print("\033[35m" + "car_model: " f'------{matches[0]}' + "\033[0m\n")
        sheet1.write(count, 3, f'{matches[0]}', style)
        print(list_m)

        for m in list_of_cars_model:
            if len(m) == 2:
                split_text = split_by2(origin)
                split_text = list(dict.fromkeys(split_text))
                for el in split_text:
                    if m.lower().strip() in el.lower().strip() or m.strip().lower() == el.lower().strip():
                        list1_m1.append(m)
        matches1 = difflib.get_close_matches(list_of_cars_model, list1_m1)
        print("\033[35m" + "car_model: " f'------{matches1[0].strip().lower()}' + "\033[0m")
        sheet1.write(count, 3, f'{matches1[0].strip().lower()}', style)
        print(list1_m1)

        list_m1 = []
        for m1 in list_of_cars_mark:

            if f' {m1.strip().lower()} ' in origin:
                list_m1.append(m1)
        m11 = max_string(list_m1)
        print("\033[35m" + "car_mark: " f'------{m11.strip().lower()}' + "\033[0m")
        sheet1.write(count, 2, f'{m11.strip().lower()}', style)

        print(list_m1)

        list_f = []
        for f in list_of_fuels:

            if f' {f.strip().lower()} ' in origin or f'{f.strip().lower()} ' in origin:
                list_f.append(f)
        f1 = max_string(list_f)
        print("\033[35m" + "car_fuel: " f'------{f1.strip().lower()}' + "\033[0m")
        sheet1.write(count, 5, f'{f1.strip().lower()}', style)
        print(list_f)
        # list_k = []

        # for k in list_of_kuzov:
        #     if f' {k.strip().lower()} ' in origin:
        #         list_k.append(k)
        # k1 = max_string(list_k)
        # print("\033[35m" + "car_kuzov: " f'------{k1.strip().lower()}' + "\033[0m")
        # sheet1.write(count, 4, f'{k1.strip().lower()}', style)
        #
        # print(list_k)
        # time.sleep(2)
        count += 1
        # time.sleep(3.5)
    wb.save(f'{file_name}.xls')
    df = pd.read_excel(f"{file_name}.xls")
    df.to_excel(f"{file_name}.xlsx", index=False)
    df = pd.read_excel(f'{file_name}.xlsx')
    df = df.dropna(axis=1, how='all')
    df.to_excel(f'{file_name}.xlsx', index=False)
    return f"{file_name}.xls"

# details(file_name='test1')
