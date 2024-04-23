from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Запись в таблицы
def written(serial, name, sclad):
    lines = 0
    with open("spisanie.csv", "a") as file:
        file.writelines('\n"' + serial + '","","' + sclad + '"')
    with open("act.csv", "r") as file:
        for line in file:
            lines += 1
    with open("act.csv", "a") as file:
        file.writelines('\n"'+ str(lines) + '","' + serial + ' ' + name + 
                        '","1","Непригодно для ремонта и эксплуатации","Уничтожить/вернуть поставщику","Требуется/не требуется"')

#Ввод количества устройств 
check = False
print("Сколько устройств нужно сканировать? (0 - выход)")
while not check:
    try:
        amount12 = int(input())
    except ValueError:
        print("Ошибка! Введите целое число устройств!")
    else:
        check = True

#Основная работа кода
work = 0
while work != amount12:

    #Обработка серийного номера
    print("Укажите серийный номер устройства (exit - выход)")
    while check:
        scan = input()
        if scan == "EXIT" or scan == "exit" or scan == "ex" or scan == "EX":
            break
        firstclick = [str(i) for i in scan]
        reverseclick = []
        for i in range(-1, -11, -1):
            try:
                x = ord(firstclick[i])
            except IndexError:
                print("Ошибка! Серийный номер содержит 10 символов!")
                check = True
                break
            else:
                if x > 64 and x < 91 or x > 47 and x < 58:
                    reverseclick.append(firstclick[i])
                    check = False
                else:
                    print("Ошибка! Встречается не допустимый символ!")
                    check = True
                    break
        serial = str()
        for i in range(len(reverseclick) - 1, -1, -1):
            serial = serial + reverseclick[i]

    #Выход из программы
    if check == True:
        break

    #Парсинг
    alltd = []
    urlname = 'http://eltex.loc/mac.php?uid=1&serial=' + serial
    urlsclad = 'https://portal-v3.eltex.loc:8445/equipment_history?sn=' + serial + '&detailed_history=false'
    responsename = requests.get(urlname)
    responsesclad = requests.get(urlsclad, verify = False)
    bsname = BeautifulSoup(responsename.text,'html.parser')
    bssclad = BeautifulSoup(responsesclad.text, 'lxml')
    temp = bsname.findAll('td', '')

    #Вывод названия устройства
    for data in temp:
        if data.text != ' ':
            alltd.append(data.text)
    try:
        print(alltd[15])
    except IndexError:
        print("Не найден серийный номер")

    #Вывод склада
    else:
        temp = bssclad.find("p", '')
        if "Промежуточный Склад" in temp.text:
            x = ""
            print("Промежуточный Склад")
        else:
            x = "Склад готовой продукции"
            print("Склад готовой продукции")
        #Вызов функции записи в таблицы
        written(serial, alltd[15], x)
        work += 1
    finally:
        check = True
print("\nЗавершение работы")