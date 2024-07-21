# 1)
# Є ось такий файл... ваша задача записати в новий файл тільки
# email'ли з доменом gmail.com (Хеш то що зліва записувати не потрібно)
print('Find gmails - Завдання 1')

try:
    with open('homework4/emails.txt', 'r') as r_f:
        with open('homework4/gmails.txt', 'w') as w_f:
            for line in r_f:
                if line.find('@gmail.com') != -1:  # або line.endswith('@gmail.com\n') або '@gmail.com' in line
                    # line = line.strip()
                    email: list[str] = line.split()
                    w_f.write(email[-1] + '\n')
except Exception as e:
    print(e)
finally:
    print('Перевірте файл gmails.txt')

# 2)
# Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# з функціоналом:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь-якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)
print('\nShopping notebook - Завдання 2')


class Purchase:
    def __init__(self, purchase_id: str, name: str, price: str) -> None:
        self.purchase_id: str = purchase_id
        self.name: str = name
        self.price: str = price

    def __str__(self) -> str:
        return f'{self.purchase_id} {self.name} {self.price}'

    def __repr__(self) -> str:
        return f'{self.purchase_id} {self.name} {self.price}'


class ShoppingNotebook:
    FILE_PATH: str = 'homework4/shopping_notebook.txt'

    @staticmethod
    def add_purchase(purchase: Purchase) -> None:
        try:
            with open(ShoppingNotebook.FILE_PATH, 'a') as a_f:
                a_f.write(str(purchase) + '\n')
        except Exception as e:
            print(e)

    @staticmethod
    def remove_purchase(purchase_id: str) -> None:
        try:
            with open(ShoppingNotebook.FILE_PATH, 'r') as r_f:
                lines = r_f.readlines()
            with open(ShoppingNotebook.FILE_PATH, 'w') as w_f:
                for line in lines:
                    if not line.startswith(str(purchase_id)):
                        w_f.write(line)
        except Exception as e:
            print(e)

    @staticmethod
    def show_purchases() -> None:
        try:
            with open(ShoppingNotebook.FILE_PATH, 'r') as r_f:
                for line in r_f:
                    print(line.strip())
        except Exception as e:
            print(e)

    @staticmethod
    def most_expensive_purchase() -> None:
        try:
            max_price: float = -1
            most_expensive: str | None = None
            with open(ShoppingNotebook.FILE_PATH, 'r') as r_f:
                for line in r_f:
                    purchase_data = line.split()
                    price: float = float(purchase_data[2])
                    if price > max_price:
                        max_price = price
                        most_expensive = line
            if most_expensive:
                print(most_expensive.strip())
        except Exception as e:
            print(e)

    @staticmethod
    def find_purchase(data: str) -> None:
        try:
            with open(ShoppingNotebook.FILE_PATH, 'r') as r_f:
                for line in r_f:
                    if data in line:
                        print(line.strip())
        except Exception as e:
            print(e)

    @staticmethod
    def show_menu() -> None:
        print('''
        add *id* *name* *price*     - додати нову покупку
        find *id | name | price*    - знайти покупку за будь-яким полем
        remove *id*     - видалити покупку за id
        show            - показати всі покупки
        most            - показати найдорожчу покупку
        menu            - вивести меню
        exit            - завершити роботу
        ''')


def main() -> None:
    ShoppingNotebook.show_menu()
    while True:
        command = input('Введіть команду: ').strip().split()
        if not command:
            continue

        action = command[0]
        match action:
            case 'add' if len(command) == 4:
                purchase_id: str = command[1]
                name: str = command[2]
                price: str = command[3]
                ShoppingNotebook.add_purchase(Purchase(purchase_id, name, price))
            case 'find' if len(command) == 2:
                ShoppingNotebook.find_purchase(command[1])
            case 'remove' if len(command) == 2:
                ShoppingNotebook.remove_purchase(command[1])
            case 'show':
                ShoppingNotebook.show_purchases()
            case 'most':
                ShoppingNotebook.most_expensive_purchase()
            case 'menu':
                ShoppingNotebook.show_menu()
            case 'exit':
                print('До побачення!')
                break
            case _:
                print('Невідома команда, спробуйте ще раз.')


main()

# 3)
# завдання зі співбесіди
# Є ось такий список:

from typing import Generator, Any

data: list[list[dict[str, Any]]] = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

# потрібно брати по черзі с кожного списку id і класти в список res,
# якщо таке значення вже є в результуючому списку, то брати наступне з того ж підсписку
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]
print('\nInterview task - Завдання 3')

res: list[int] = []


# аналогія до човникового бігу (приклад з лекції)
def gen(my_list: list[dict[str, Any]]) -> Generator:
    for item in my_list:
        yield item


lists: list[Generator] = [gen(sublist) for sublist in data]

while lists:
    current_list: Generator = lists.pop(0)

    try:
        # print(next(current_list))
        item: dict[str, Any] = next(current_list)
        if item['id'] not in res:
            res.append(item['id'])
            lists.append(current_list)
        else:
            lists.insert(0, current_list)
    except StopIteration:
        pass

    print(res)

# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i} - Team 1'
#
#
# def gen2(n):
#     for i in range(1, n + 1):
#         yield f'{i} - Team 2'
#
#
# teams = [gen1(8), gen2(8)]
#
# while teams:
#     player = teams.pop(0)
#
#     try:
#         print(next(player))
#         teams.append(player)
#     except StopIteration:
#         pass
