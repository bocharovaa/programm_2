import requests


#выведем список существующих id
res = requests.get("http://127.0.0.1:3000/api/services/0")
new_id = 0 #переменная для хранения номера нового id
for n in res.json():#перебираем id
    new_id = max(new_id, int(n)) #находим из них максимальный

new_id = new_id + 1 #новый id это максимальный из существубщих +1

#запрос на ввод данных от пользователя
print("Введите название услуги")
name = input()
print("Введите cкорость тарифа")
speed = input()

res = requests.post("http://127.0.0.1:3000/api/services/" + str(new_id),  #запрос POST, где последняя цифра обозначает id интернет услуги, которую добавляем
                    json = {'name': name, 'speed(mb/s)': speed})  #далее указываем параметры записи для добавления

print(res.json())
input()
