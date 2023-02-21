import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


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
    driver.get('https://auto.ru/')
    driver.find_element(By.XPATH, '/html/body/div/div[4]/a[1]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,
                        '/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[6]/div').click()
    link1 = []
    mark1 = []

    link_ = []
    try:
        links = driver.find_elements(By.TAG_NAME, 'a')
        for s in links:
            s1 = s.get_attribute('href')
            if s1.startswith('https://auto.ru/cars/') or s1.startswith('https://auto.ru/catalog/cars/'):
                # print(s1)
                link_.append(s1)
    except:
        print("tugadi linkla")
    for i in link_[22:]:
        link1.append(i)
    try:
        i = 1
        k = 1
        while True:
            mark_car = driver.find_element(By.XPATH,
                                           f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[{k}]/a[{i}]/div[1]').text
            # link = driver.find_elements(By.XPATH,
            #                             "/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]")
            # for i in link:
            #     href = i.get_attribute('href')
            #     print(href)
            # link = driver.find_element(By.TAG_NAME, 'a')
            # href = link.get_attribute('href')
            # print(href)
            # print(i)
            mark1.append(mark_car)
            i += 1

            # print(mark_car)
            if i == 39 or i == 76 or i == 114 or i == 152 or i == 190:
                i = 1
                k += 1

                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/a[2]/div[1]').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/a[1]/div[1]').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/a[2]/div[1]').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/a[1]/div[1]').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[3]/a[2]/div[1]').text

                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[2]/a[1]/div').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[2]/a[2]/div').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[3]/a[1]/div').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[3]/a[2]/div').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[4]/a[1]/div').text
                # f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[4]/a[2]/div').text
    except:
        try:
            # print('tugadi!!!')

            i = 1
            k = 2
            while True:
                # driver.get('https://auto.ru/')
                # driver.find_element(By.XPATH, '/html/body/div/div[4]/a[1]').click()
                # time.sleep(5)
                # driver.find_element(By.XPATH,
                #                     '/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[6]/div').click()
                catalog_mark = driver.find_element(By.XPATH,
                                                   f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[3]/div[{k}]/a[{i}]/div').text
                # link = driver.find_element(By.XPATH,
                #                            f'/html/body/div[2]/div/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[{k}]/a[{i}]/div[1]').find_element(
                #     By.TAG_NAME, 'a')
                # href = link.get_attribute('href')
                # print(href)

                # print(i)
                # print(k)
                i += 1
                # print(catalog_mark)
                mark1.append(catalog_mark)
                if i == 26 or i == 52 or i == 78 or i == 104 or i == 130:
                    i = 1
                    k += 1
        except:
            pass
    for j, k in zip(link1, mark1):
        print(j, '-->', k)

my_selen()
