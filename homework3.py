from abc import ABC, abstractmethod

# 1)
# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
print("Rectangle - Завдання 1")


class Rectangle:
    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def area(self) -> int | float:
        return self.x * self.y

    def __add__(self, other) -> int | float:
        if isinstance(other, Rectangle):
            return self.area() + other.area()

    def __sub__(self, other) -> int | float:
        if isinstance(other, Rectangle):
            return self.area() - other.area()

    def __eq__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __ne__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() != other.area()

    def __gt__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() > other.area()

    def __lt__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __len__(self) -> int | float:
        return 2 * (self.x + self.y)

    def __str__(self):
        return f"(Rectangle: x={self.x}, y={self.y})"


rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)

print('rec1>', rec1)
print('rec2>', rec2)

print('rec1.area()>', rec1.area())
print('rec2.area()>', rec2.area())

print('rec1 + rec2', rec1 + rec2)
print('rec1 - rec2', rec1 - rec2)

print('rec1 == rec2', rec1 == rec2)
print('rec1 != rec2', rec1 != rec2)
print('rec1 > rec2', rec1 > rec2)
print('rec1 < rec2', rec1 < rec2)

print('len(rec1)>', len(rec1))
print('len(rec2)>', len(rec2))

#############################################################################################################

# 2)
# створити клас Human (name, age)
# створити два класи Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка,
# а також метод котрий буде приймати список попелюшок, та шукати ту саму

# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів класу
# також має бути метод класу який буде виводити це значення
print('\nPrince & Cinderella - Завдання 2')


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Cinderella(Human):
    __count: int = 0

    def __init__(self, name: str, age: int, foot_size: int | float):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls) -> int:  # або cinderellas_count
        return cls.__count


class Prince(Human):
    def __init__(self, name: str, age: int, boot_size: int | float):
        super().__init__(name, age)
        self.boot_size = boot_size

    def find_cinderella(self, cinderella_list: list[Cinderella]) -> Cinderella | None:
        for cinderella in cinderella_list:
            if isinstance(cinderella, Cinderella) and cinderella.foot_size == self.boot_size:
                return cinderella


prince: Prince = Prince('Robert', 20, 5)

cinderellas: list[Cinderella] = [
    Cinderella('Anna', 19, 3),
    Cinderella('Bob', 22, 4),
    Cinderella('Carol', 21, 6),
    Cinderella('Dave', 20, 3),
    Cinderella('Eve', 19, 5),
    Cinderella('Frank', 25, 6),
]

print('Our prince:', prince)
print('Count of cinderellas:', Cinderella.get_count())
found_cinderella = prince.find_cinderella(cinderellas)
print('Found cinderella:', found_cinderella if found_cinderella else "No Cinderella found...")

#############################################################################################################

# 3)
# 1. Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2. Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3. Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то
# що передають є класом Book або Magazine інакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))

# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()

# для перевірки класів використовуємо метод isinstance, приклад:

# user = User('Max', 15)
# shape = Shape()

# isinstance(max, User) -> True
# isinstance(shape, User) -> False

print('\nMagazines & Books - Завдання 3')


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self) -> None:
        print('Book:', self.name)


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self) -> None:
        print('Magazine:', self.name)


class Main:
    printable_list: list[Book | Magazine] = []

    @classmethod
    def add(cls, book: Book | Magazine) -> None:
        if isinstance(book, Book) or isinstance(book, Magazine):
            cls.printable_list.append(book)

    @classmethod
    def show_all_magazines(cls) -> None:
        for magazine in cls.printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()

    @classmethod
    def show_all_books(cls) -> None:
        for book in cls.printable_list:
            if isinstance(book, Book):
                book.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
