import time

import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

# from django.db import connections as con

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

connect = psycopg2.connect(
    dbname="postgres", user="postgres", password="0852", host="127.0.0.1",
    port="5432")
# cursor = con['default'].cursor()
cursor = connect.cursor()


# def telebots(mess):
#     requests.get(
#         url=f"https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")

# def telebots_2(mess, mess1):
#     requests.get(
#         url=f"https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}\n{mess1}")

def my_selen():
    driver = webdriver.Chrome(options=options)
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    driver.get(
        'https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=audi&maximum_distance=20&mileage_max=&page_size=20&sort=best_match_desc&year_max=&year_min=&zip=')
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/section[1]/div[2]/div/div[4]/select').click()
    try:
        i = 1
        while True:
            # try:
            name_mark = driver.find_element(By.XPATH,
                                            f'/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/section[1]/div[2]/div/div[4]/select/optgroup[1]/option[{i}]').text
            print(name_mark)
            cursor.execute(
                "insert into mark (mark_name) values (%s) ON CONFLICT DO NOTHING",
                (name_mark,))
            connect.commit()
            cursor.execute('select id from mark where mark_name=%s', (name_mark,))
            mark_id = cursor.fetchone()[0]
            # except:
            #     print('mark topilmadi')
            #     continue
            # print('last_id', mark_id)
            # time.sleep(1)
            driver.find_element(By.XPATH,
                                f'/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/section[1]/div[2]/div/div[4]/select/optgroup[1]/option[{i}]').click()
            time.sleep(1)
            try:
                for j in range(1, 1000):
                    print(j)
                    # try:
                    models = driver.find_element(By.XPATH,
                                                 f'/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/div[2]/div/div[{j}]').text
                    print(models)
                    cursor.execute("INSERT INTO model1 (model_name,mark_name_id) VALUES (%s,%s) on conflict do nothing",
                                   (models, mark_id))
                    connect.commit()
                        # time.sleep(1)
                    # except:
                    #     print('models topilmadi')
                    #     continue
            except:
                print('finished models')
            i += 1
    except:
        # except Exception as e:
        print('error2')
        # try:
        #     k = 1
        #     while True:
        #         try:
        #             name_mark1 = driver.find_element(By.XPATH,
        #                                              f'/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/section[1]/div[2]/div/div[4]/select/optgroup[2]/option[{k}]').text
        #             print(name_mark1)
        #             driver.find_element(By.XPATH,
        #                                 f'/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/section[1]/div[2]/div/div[4]/select/optgroup[1]/option[{k}]').click()
        #             cursor.execute(
        #                 "insert into mark (mark_name) values (%s) ON CONFLICT DO NOTHING",
        #                 (name_mark1,))
        #             connect.commit()
        #             cursor.execute('select id from mark where mark_name=%s', (name_mark1,))
        #             mark_id = cursor.fetchone()[0]
        #         except:
        #             print('mark1 topilmadi')
        #             continue
        #         # time.sleep(1)
        #
        #         try:
        #             for j in range(1, 1000):
        #                 print(j)
        #                 try:
        #                     models1 = driver.find_element(By.XPATH,
        #                                                   f'/html/body/section/div[2]/div[5]/div/div[4]/div[2]/form/div[2]/div/div[{j}]').text
        #                     print(models1)
        #                     cursor.execute(
        #                         "INSERT INTO model1 (model_name,mark_name_id) VALUES (%s,%s) on conflict do nothing",
        #                         (models1, mark_id))
        #                     connect.commit()
        #                 except:
        #                     print('models1 topilmadi')
        #                     continue
        #         except:
        #             print('finished models')
        #         k += 1
        # except:
        #     print('tugadi')


# my_selen()
