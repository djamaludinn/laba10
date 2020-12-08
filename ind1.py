# -*- coding: utf-8 -*-

# Вариант 18. Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.

import sys


def new_add(market, shop, product, price):
    # Создать словарь.
    markets = {
        'shop': shop,
        'product': product,
        'price': price,
    }

    # Добавить словарь в список.
    market.append(markets)
    # Отсортировать список в случае необходимости.
    if len(market) > 1:
        market.sort(key=lambda item: item.get('shop', ''))

def new_list(market):
    table = []
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Магазин",
            "Товар",
            "Стоимость в руб."
        )
    )
    table.append(line)


    # Вывести данные о всех товарах.
    for idx, markets in enumerate(market, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                markets.get('shop', ''),
                markets.get('product', ''),
                markets.get('price', 0)
            )
        )

    table.append(line)

    return '\n'.join(table)


def new_select(market):
    # Инициализировать результат.
    result = []
    # Проверить сведения товаров из списка.
    for markets in market:
        result.append(markets)

    return result


if __name__ == '__main__':
    # Список товаров.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            shop = input("Название магазина? ")
            product = input("Название товара? ")
            price = int(input("Стоимость товара в руб.? "))

            new_add(market, shop, product, price)

        elif command == 'list':
            print(list(market))

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера.
            parts = command.split(maxsplit=1)
            # Получить список товаров.
            selected = new_select(markets, int(parts[1]))
            # Вывод списка товаров.
            if selected:
                for idx, markets in enumerate(selected, 1):
                    print('{:>4}: {}'.format(idx, markets.get('name', '')))
            else:
                print("Товар не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <товар> - информация о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)






