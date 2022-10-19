import requests

print("Введите цифру номера услуги(0 - все)")
input_ = input()
request = "http://127.0.0.1:3000/api/services/" + input_


#запрос GET, где последняя цифра обозначает id интернет услуги, которую хотим получить(0 - все услуги выведутся)
res = requests.get(request)

print(res.json())
input()