#Необходимые библиотеки
import argparse
from json import load
from functions import*

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--create", type=str, help=">>>>Создать пустой файл данных для <<<<")
    group.add_argument("-fc", "--findincity", type=str, help=">>>>Найти клиента по городу прибытия<<<<")
    group.add_argument("-fs", "--findsurename", type=str, help=">>>>Найти клиента по фамилии<<<<")
    group.add_argument("-fn", "--findcompanyname", type=str, help=">>>>Найти клиента по имени компании перевозчика<<<<")
    group.add_argument("-i", "--insert", type=str, help=">>>>Внести данные<<<<")
    group.add_argument("-d", "--delete", type=str, help=">>>>Удалить данные<<<<") 
    group.add_argument("-p", "--print", type=str, help=">>>>Вывести данные<<<<")
    args = parser.parse_args()

    if args.create:
        save([], args.create)
    
    elif args.findincity:
        data = load(args.findincity)
        in_city = input('Введите город прибытия: ')
        result = find_in_city(data, in_city)
        if result:
            for item in result:
                formatter(item)
        else:
            print(f'По запросу {in_city} ничего не найдено!')

    elif args.findsurename:
        data = load(args.findsurename)
        surename = input('Введите фамилию клиента: ')
        result = find_surename(data, surename)
        if result:
            for item in result:
                formatter(item)
        else:
            print(f'По запросу {surename} ничего не найдено!')

    elif args.findcompanyname:
        data = load(args.findcompanyname)
        company_name = input('Введите имя перевозчика: ')
        result = find_in_city(data, company_name)
        if result:
            for item in result:
                formatter(item)
        else:
            print(f'По запросу {company_name} ничего не найдено!')

    elif args.insert:
        data = load(args.insert)
        inserted_client = read()
        try:
            insert(data, inserted_client)
        except InsertionError as i:
            print('Невозможно добавить такого клиента!')
        finally:
            save(data, args.insert)

    elif args.delete:
        data = load(args.delete)
        deleted_client = read()
        try:
            data = delete(data, deleted_client)
        except DeletionError:
            print('Невозможно удалить такого клиента!')
        finally:
            save(data, args.delete)

    elif args.print:
        data = load(args.print)
        if data:
            for item in data:
                formatter(item)
    
    else:
        print('Неизвестная команда! Помощь: -h')

if __name__ == "__main__":
    main()
