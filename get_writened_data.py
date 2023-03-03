from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import psycopg2

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

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

url = "https://languagetool.org/"
driver.get(url)
for i in row:
    row_id = i[0]
    row_name = i[1]
    print(row_name)
    try:
        time.sleep(1)
        message = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div[3]/section/div/div[2]/div[2]')
        # time.sleep(1)
        message.click()
        # time.sleep(1)
        # try:
        delete = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/div[3]/section/div/div[1]/div/div[2]/div/span[2]')
        delete.click()
        # except:
        #     print('toza')
        message.send_keys(f"{row_name}")
        # time.sleep(1)
    except:
        print('soz kiritilmadi\n')
        # message.clear()
        # time.sleep(1)
        continue


# time.sleep(500000)
