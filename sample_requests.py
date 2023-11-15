import requests

url = "http://localhost:8000/form"

# Запрос 1
data1 = {"user_name": "Dima", "user_phone": "+79099555555"}
response1 = requests.post(url, data=data1)
print("Response 1:", response1.text)

# Запрос 2
data2 = {"user_email": "dima@admin.com", "user_phone": "+79099555555"}
response2 = requests.post(url, data=data2)
print("Response 2:", response2.text)

# Запрос 3
data3 = {"important_date": "2022-01-01", "user_phone": "+79099555555"}
response3 = requests.post(url, data=data3)
print("Response 3:", response3.text)

# Запрос 4
data4 = {"user_email": "dima@admin.com", "user_phone": "9099555555"}
response4 = requests.post(url, data=data4)
print("Response 4:", response4.text)
