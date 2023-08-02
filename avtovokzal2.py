#Необходимые библиотеки
from datetime import datetime, date, time #модуль дата-время
from dataclasses import dataclass, asdict #модуль датакласса #1

@dataclass(slots = True, frozen = True)
class Bus_Station_Client_Info:
    """
    Класс-контейнер для хранения данных о клиентах автовокзала
    """
    name: str #Имя
    surename: str #Фамилия
    third_name: str #Отчество (если нет - пустая строка)

    born_date: str #Дата рождения в формате гггг-мм-дд
    pass_id: int #Серия паспорта
    pass_num: int #Номер паспорта

    from_city: str #Город отправления
    in_city: str #Город прибытия

    arrive_datetime: str #Дата и время отправления
    travel_time: int #Примерное время в пути

    place_num: int #Номер посадочного места 

    company_name: str #Название компании перевозчика

    def to_dict(self):
        """
        Преобразование Dataclass в Dict
        """
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        return Bus_Station_Client_Info(name = data['name'], 
                                       surename = data['surename'], 
                                       third_name = data['third_name'],
                                       born_date = data['born_date'],
                                       pass_id = data['pass_id'],
                                       pass_num = data['pass_num'],
                                       from_city = data['from_city'],
                                       in_city = data['in_city'],
                                       arrive_datetime = data['arrive_datetime'],
                                       travel_time = data['travel_time'],
                                       place_num = data['place_num'],
                                       company_name = data['company_name'])



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