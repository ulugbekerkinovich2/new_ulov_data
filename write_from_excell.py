from datetime import datetime

import openpyxl
import pandas
import pandas as pd
import psycopg2
import requests
import xlrd

from get_data import details

# from django.db import connections

connect = psycopg2.connect(
    dbname="car_com2", user="postgres", password="0852", host="127.0.0.1",
    port="5432")
# connect = connections
connect.autocommit = True
cursor = connect.cursor()


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAFeaNW1dtleNNM4DDPBnvpC7XdtTZ687mo/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


def my_func():
    telebots('get files from excell')
    cursor.execute("SELECT file FROM upload_file")
    files = cursor.fetchall()[-1][0]
    print(files, '-----------shu file')
    cursor.execute("SELECT write_file_name FROM upload_file")
    file_name = cursor.fetchall()[-1][0]
    # print(file_name)
    excel_data_df = pd.read_excel(f"media/{files}")
    num_rows = excel_data_df.shape[0]
    # print(num_rows)
    now = datetime.now()
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")

    create_table_query = f"CREATE TABLE {file_name} (id SERIAL PRIMARY KEY, description TEXT);"
    cursor.execute(create_table_query)

    try:
        for i in range(num_rows):
            data = excel_data_df.iloc[i, 0]
            print(i, ' ', data)
            print('\n')
            cursor.execute(f"INSERT INTO {file_name} (description) VALUES (%s)", (data,))
            connect.commit()
    except:
        print('tugadi')

    file_origin = details(file_name)

    def telebots1(mess, file_path):
        # Telegram API endpoint for sending documents
        endpoint = "https://api.telegram.org/bot5082135962:AAFeaNW1dtleNNM4DDPBnvpC7XdtTZ687mo/sendDocument"

        # Define the chat ID and message text
        chat_id = "935920479"
        message = {"chat_id": chat_id, "caption": mess, "parse_mode": "HTML"}

        # Read the file content and add it to the request
        with open(file_path, "rb") as f:
            files = {"document": f}
            response = requests.post(endpoint, data=message, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            telebots('file sent successfully!')
            print("file sent successfully!")
        else:
            telebots(f"Failed to send message and file. Response: {response.text}")
            print(f"Failed to send message and file. Response: {response.text}")

    telebots1(files, file_origin)
# my_func()
# import requests

# def telebots1(file_path, mess):
#     # Telegram API endpoint for sending documents
#     endpoint = "https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendDocument"
#
#     # Define the chat ID and message text
#     chat_id = "935920479"
#     message = {"chat_id": chat_id, "caption": mess, "parse_mode": "HTML"}
#
#     # Read the file content
#     with open(file_path, "rb") as f:
#         # Use tqdm to display the progress bar
#         file_size = len(f.read())
#         f.seek(0)
#         pbar = tqdm(total=file_size, unit="B", unit_scale=True)
#         for chunk in f:
#             # Update the progress bar
#             pbar.update(len(chunk))
#
#             # Send the file chunk to the Telegram API
#             response = requests.post(endpoint, data=message, files={"document": chunk})
#
#             # Check if the request was successful
#             if response.status_code != 200:
#                 telebots(f"Failed to send chunk. Response: {response.text}")
#                 pbar.write(f"Failed to send chunk. Response: {response.text}")
#                 break
#             else:
#                 telebots("Message and file sent successfully!")
#
#         # Close the progress bar
#         pbar.close()


# import time
# from tqdm import tqdm
#
#
# def telebots1(file_path, mess):
#     # Telegram API endpoint for sending documents
#     endpoint = "https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendMessage"
#
#     # Define the chat ID and message text
#     chat_id = "935920479"
#     message = f"{mess} 0%"
#
#     # Send the initial message
#     requests.get(url=f"{endpoint}?chat_id={chat_id}&parse_mode=HTML&text={message}")
#
#     # Read the file content
#     with open(file_path, "rb") as f:
#         # Use tqdm to display the progress bar
#         file_size = len(f.read())
#         f.seek(0)
#         pbar = tqdm(total=file_size, unit="B", unit_scale=True)
#         for chunk in f:
#             # Update the progress bar
#             pbar.update(len(chunk))
#
#             # Update the message text
#             progress = int(pbar.n / file_size * 100)
#             message = f"{mess} {progress}%"
#
#             # Send the updated message
#             response = requests.get(url=f"{endpoint}?chat_id={chat_id}&parse_mode=HTML&text={message}")
#
#             # Check if the request was successful
#             # if response.status_code != 200:
#             #     telebots(f"Failed to send chunk. Response: {response.text}")
#             #     pbar.write(f"Failed to send chunk. Response: {response.text}")
#             #     break
#             # else:
#             #     telebots("Message and file sent successfully!")
#
#             # Wait for a short period of time
#             time.sleep(0.1)
#
#         # Close the progress bar
#         pbar.close()

# import time
# from tqdm import tqdm


# def telebots1(file_path, mess):
#     # Telegram API endpoint for sending documents
#     endpoint = "https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendMessage"
#
#     # Define the chat ID and message text
#     chat_id = "935920479"
#     message = f"{mess} 0%"
#
#     # Send the initial message
#     requests.get(url=f"{endpoint}?chat_id={chat_id}&parse_mode=HTML&text={message}")
#
#     # Read the file content
#     with open(file_path, "rb") as f:
#         # Use tqdm to display the progress bar
#         file_size = len(f.read())
#         f.seek(0)
#         pbar = tqdm(total=file_size, unit="B", unit_scale=True)
#         for chunk in f:
#             # Update the progress bar
#             pbar.update(len(chunk))
#
#             # Update the message text
#             progress = int(pbar.n / file_size * 100)
#             message = f"{mess} {progress}%"
#
#             # Send the updated message
#             response = requests.get(url=f"{endpoint}?chat_id={chat_id}&parse_mode=HTML&text={message}")
#
#             # Check if the request was successful
#             if response.status_code != 200:
#                 pbar.write(f"Failed to send message. Response: {response.text}")
#                 break
#
#             # Wait for a short period of time
#             time.sleep(0.1)
#
#         # Close the progress bar
#         pbar.close()
#
#     # Wait for a short period of time after uploading the file
#     time.sleep(1)
#     message = f"{mess} 100%"
#     requests.get(url=f"{endpoint}?chat_id={chat_id}&parse_mode=HTML&text={message}")


# telebots1(files, file_name + f"_{now_time}")

# Commit the changes
# my_func()
