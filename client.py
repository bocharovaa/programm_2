import requests
import json

def get_request(url):
    print("Введите цифру номера услуги(0 - все)")
    input_ = input()


    request = url + input_
    #запрос GET, где последняя цифра обозначает id интернет услуги, которую хотим получить(0 - все услуги выведутся)
    res = requests.get(request)
    print(res.json())


def post_request(url):
    res = requests.get(url +"0")
    new_id = 0              #переменная для хранения номера нового id
    for n in res.json():    #перебираем id
        new_id = max(new_id, int(n)) #находим из них максимальный
    
    new_id = new_id + 1 #новый id это максимальный из существубщих +1
    
    #запрос на ввод данных от пользователя
    print("Введите название услуги")
    name = input()
    print("Введите cкорость тарифа")
    speed = input()
    
    res = requests.post(url + str(new_id),  #запрос POST, где последняя цифра обозначает id интернет услуги, которую добавляем
                        json = {'name': name, 'speed(mb/s)': speed})  #далее указываем параметры записи для добавления
    print(res.json())

def main():
    url = "http://127.0.0.1:3000/api/services/"
    print("Выберите запрос:")
    print("1: Get")
    print("2: Post")
    request_number = int(input())
    
    while request_number != 9:
        if request_number == 1:
            get_request(url)
        if request_number == 2:
            post_request(url)
        
        print("Выберите запрос:")
        print("1: Get")
        print("2: Post")
        request_number = int(input())
        
if __name__ == "__main__":
    main()