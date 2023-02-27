import time

import psycopg2
import requests
import xlwt

# from write_from_excell import telebots

connect = psycopg2.connect(
    dbname="postgres", user="postgres", password="0852", host="127.0.0.1",
    port="5432")


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAFeaNW1dtleNNM4DDPBnvpC7XdtTZ687mo/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


def details1(file_name):
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
    # print(data)
    data = list(set(data))
    sheet1.write(0, 0, 'Наим. Товара')
    sheet1.write(0, 1, 'Марка')
    sheet1.write(0, 2, 'Модель')
    sheet1.write(0, 3, 'Тип кузова')
    sheet1.write(0, 4, 'Тип топливо')
    count = 1
    style = xlwt.easyxf('align: wrap yes')
    for i in data:
        print(i)
        print(count)
        sheet1.write(count, 1, f'{i.strip().lower()}', style)
        # print(i)
        print('\n')
        belgi = [',', '(', ')', '-', '+', '=', '#', '"', '"', '.', ':', ';', "'", "'", '"', ",", '/', '"\"']

        def max_string(strings):
            max_length = 0
            max_string = ""
            for s in strings:
                if len(s) > max_length:
                    max_length = len(s)
                    max_string = s
            return max_string

        def remove_symbols(text, symbols):
            for symbol in symbols:
                text = text.replace(symbol, ' ')
            return text

        print(remove_symbols(i, belgi))
        origin = remove_symbols(i, belgi)
        list_m = []

        # time.sleep(50)
        for m in list_of_cars_model:
            if m.isnumeric():
                continue

            if f' {m.strip().lower()} ' in origin:
                list_m.append(m)
        maxim = max_string(list_m)
        print("\033[35m" + "car_model: " f'------{maxim.strip().lower()}' + "\033[0m")
        sheet1.write(count, 3, f'{maxim.strip().lower()}', style)
        print(list_m)

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
        list_k = []

        # for k in list_of_kuzov:
        #
        #     if f' {k.strip().lower()} ' in origin:
        #         list_k.append(k)
        # k1 = max_string(list_k)
        # print("\033[35m" + "car_kuzov: " f'------{k1.strip().lower()}' + "\033[0m")
        # sheet1.write(count, 4, f'{k1.strip().lower()}', style)

        print(list_k)
        # time.sleep(2)
        count += 1
        # time.sleep(4)
    wb.save(f'{file_name}.xls')

    return f"{file_name}.xls"


# details(file_name='test')
