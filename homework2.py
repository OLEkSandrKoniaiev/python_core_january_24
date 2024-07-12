from typing import Callable

# 1) & 2)
print("Завдання 1 & 2")  # Closure


def notebook() -> tuple[Callable[[str], None], Callable[[], None]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> None:
        nonlocal todo_list
        if len(todo_list) == 0:
            print('> Цей список пустий')
        else:
            print('> Елементи списку: ')
            for index, todo in enumerate(todo_list):
                print(index + 1, '. ', todo, sep='')

    return add_todo, get_all


add, get = notebook()
get()
add('Перше завдання')
get()
add('Друге завдання')
get()

# 3)
print('\nЗавдання 3')


def numbers_bits_sum(num: int | str) -> str:
    bits: list[str] = []
    if isinstance(num, int):
        str_num: str = str(num)
    else:
        str_num = num
    num_len: int = len(str_num) - 1

    for bit in str_num:
        if bit == '0':
            num_len -= 1
            continue
        bits.append(bit + '0' * num_len)
        num_len -= 1

    return ' + '.join(bits)


numbers: list[int] = [12, 42, 943, 70304, 82003, 290045]
for number in numbers:
    print(f'({number})> {numbers_bits_sum(number)}')

# 4)
print('\nЗавдання 4')


def decor(func: Callable[[], None]) -> Callable[[], None]:
    count: int = 0

    def inner():
        nonlocal count
        count += 1
        print(f'count: {count}')
        func()
        print('-' * 10)

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func2()
