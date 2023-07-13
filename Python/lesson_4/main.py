from random import randint


def check_data(*, message: str) -> str:
    while True:
        number = input(f'{message}: ')
        # Проверка на пустату и отсутствие букв
        if number.isdigit():
            return number
        else:
            print(
                '\nНе корректные данные! (Только натуральное число: N > 0...)\nДля выхода нажать Ctrl + C\n')


"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

Киррил да, это звиздец. Кто пишет эти условия для этих абстракций, покалатить его палкой. Надеюсь не мадам.
"""


def repeat_numbers(*, first: int, second: int):
    """ """
    print(first_list := set([randint(0, 30) for _ in range(first)]))
    print(second_list := set([randint(0, 30) for _ in range(second)]))
    repeat_numbers = first_list & second_list
    print(f'Repeat numbers: {sorted(repeat_numbers)}\n')


"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""


def max_berries():
    """ number_kysts :D """
    number_kysts = randint(5, 15)
    print(berries := [randint(0, number_kysts) for _ in range(number_kysts)])
    max_berries = 0
    for i, v in enumerate(berries):
        max_b = berries[(i-1) % number_kysts] + berries[i % number_kysts] + berries[(i+1) % number_kysts]
        if max_b > max_berries:
            max_berries = max_b
    print(f'Max sum berries: {max_berries}\n')


def main():
    """ """
    print(f"\nЗадача 22. Введите натуральные числа\n{'-'*40}")
    repeat_numbers(first=int(check_data(message='Введите первое число')),
                   second=int(check_data(message='Введите второе число')))
    
    print(f"\nЗадача 24. Максимальное число ягод\n{'-'*40}")
    max_berries()


if __name__ == '__main__':
    main()
