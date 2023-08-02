#Необходимые библиотеки
from avtovokzal2 import*
from typing import List
from genericpath import samefile
import json

#Форматирование данных
def formatter(*args: Bus_Station_Client_Info) -> str:
    """
    Функция для форматирования составных данных Dataclass. 
    Преобразует Dataclass в str
    """
    for arg in args:
        print( 
                f'Информация о клиенте автовокзала:\n'
                f'ФИО: {arg.surename} {arg.name} {arg.third_name}\n'
                f'Дата рождения: {arg.born_date}\n'
                f'Серия и номер паспорта: {arg.pass_id}№{arg.pass_num}\n'
                f'Место отправления: {arg.from_city}\n'
                f'Место прибытия: {arg.in_city}\n'
                f'Дата и время отправления: {arg.arrive_datetime}\n'
                f'Время в пути: {arg.travel_time}\n'
                f'Место: {arg.place_num}\n'
                f'Перевозчик: {arg.company_name}\n',
                sep = '-' * 40 + '\n', 
                end = '-' * 40 + '\n')
        
#Поиск по критериям
def find_in_city(data: List[Bus_Station_Client_Info], in_city: str) -> List[Bus_Station_Client_Info]:
    """
    Функция для поиска клиента по городу прибытия автобуса
    """
    return [item for item in data if item.in_city == in_city]

def find_surename(data: List[Bus_Station_Client_Info], surename: str) -> List[Bus_Station_Client_Info]:
    """
    Функция для поиска клиента по городу прибытия автобуса
    """
    return [item for item in data if item.surename == surename]

def find_company(data: List[Bus_Station_Client_Info], company: str) -> List[Bus_Station_Client_Info]:
    """
    Функция для поиска клиента по городу прибытия автобуса
    """
    return [item for item in data if item.company_name == company]

#Добавление-удаление
class InsertionError(Exception):
    """
    Возникает в случае, если клиент уже есть в базе автовокзала
    """
    pass

class DeletionError(Exception):
    """
    Возникает в случае, если клиента нет в базе автовокзала
    """
    pass

def insert(data: List[Bus_Station_Client_Info], client: Bus_Station_Client_Info) -> List[Bus_Station_Client_Info]:
    """
    Функция для добавления клиента в базу данных автовокзала
    """
    if client in data:
        raise InsertionError
    else:
        data.append(client)
        return data
    
def delete(data: List[Bus_Station_Client_Info], client: Bus_Station_Client_Info) -> List[Bus_Station_Client_Info]:
    """
    Функция для удаления клиента из базы данных автовокзала
    """
    if client not in data:
        raise DeletionError
    else:
        return [item for item in data if item != client]
    
#Load-Save
def load(filename: str) -> List[Bus_Station_Client_Info]:
    """
    Функция для чтения файлов в формате JSON
    """
    with open(filename, mode = 'r') as file:
        data = json.load(file)
    return [Bus_Station_Client_Info.from_dict(item) for item in data]

def save(data: List[Bus_Station_Client_Info], filename: str):
    """
    Функция для записи файлов в формате JSON
    """
    data = [item.to_dict() for item in data]

    with open(filename, mode = 'w') as file:
        json.dump(data, file)

def read() -> Bus_Station_Client_Info:
    """
    Функция для чтения информации о клиенте из консоли
    """
    name = input('Введите имя клиента: ')
    surename = input('Введите фамилию клиента: ')
    third_name = input('Введите отчество клиента (если нет - пропуск): ')

    born_date = datetime.strftime(date(year = int(input('Год рождения клиента: ')),
                                    month = int(input('Месяц рождения клиента: ')),
                                    day = int(input('День рождения клиента: '))),
                                    format = '%Y/%m/%d')
    pass_id = int(input('Введите серию паспорта клиента: '))
    pass_num = int(input('Введите номер паспорта клиента: '))

    from_city = input('Введите город отправления: ')
    in_city = input('Введите город прибытия: ')

    arrive_datetime = datetime.strftime(datetime(year = int(input('Год отправления: ')),
                                    month = int(input('Месяц отправления: ')),
                                    day = int(input('День отправления: ')),
                                    hour = int(input('Время отправления (часы): ')),
                                    minute = int(input('Время отправления (минуты): '))),
                                    format = '%Y/%m/%d')
    travel_time = int(input('Время в пути (часов): '))

    place_num = int(input('Введите номер посадочного места: '))

    company_name = input('Введите перевозчика: ')

    return Bus_Station_Client_Info(name, surename, third_name, 
                                   born_date, pass_id, pass_num,
                                    from_city, in_city,
                                    arrive_datetime, travel_time,
                                    place_num, company_name)

if __name__ == "__main__":
    first = Bus_Station_Client_Info('Кулбар', 'Софтвар', 'Улугмы', 
                                    datetime.strftime(date(year = 2003, month = 11, day = 16), '%Y/%m/%d'), 
                                    11, 5218790,
                                    'Семей', 'Барнаул', 
                                    datetime.strftime(datetime(year = 2023, month = 8, day = 4, hour = 8, minute = 30), '%Y/%m/%d │ %H:%M'),
                                    8, 1, 'ИП Камышев Д. В.')
    
    second = Bus_Station_Client_Info('Окунь', 'Речной', '', 
                                    datetime.strftime(date(year = 2002, month = 10, day = 30), '%Y/%m/%d'), 
                                    42, 1952052,
                                    'Семей', 'Омск', 
                                    datetime.strftime(datetime(year = 2023, month = 8, day = 24, hour = 7, minute = 0), '%Y/%m/%d │ %H:%M'),
                                    14, 17, 'ИП Камышев Д. В.')
    
    third = Bus_Station_Client_Info('Кратос', 'Спартанец', 'Зевсович', 
                                    datetime.strftime(date(year = 1950, month = 7, day = 12), '%Y/%m/%d'),
                                    12, 7204260, 
                                    'Барнаул', 'Сочи', 
                                    datetime.strftime(datetime(year = 2023, month = 6, day = 30, hour = 12, minute = 0), '%Y/%m/%d │ %H:%M'),
                                    6, 23, 'Авиакомпания "Аэрофлот"')
    data = [first, second, third]

    new = read()
    data.append(new)
    save(data, 'data.json')
    DATA = load('data.json')
    for element in DATA:
        formatter(element)