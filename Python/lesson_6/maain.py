from random import randint

"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""


def arithmetic_progression(first_element: int, raznost: int, total_elemnts: int) -> list[int]:
    """ """
    return [first_element + (i - 1) * raznost for i in range(1, total_elemnts)]


"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""


def elements_index(start: int, finish: int, elements: list) -> list[int]:
    """ """
    return [elements.index(i) for i in elements if start < i < finish]


def main():
    """ """
    first = razn = randint(2, 5)
    total, start, finish = randint(10, 15), 10, 30

    response_prog = arithmetic_progression(first_element=first, raznost=razn, total_elemnts=total)
    print(f"\nЗадача 30. Арифметическая прогрессия\n{'-'*40}\nПервый: {first} Разность: {razn} Кол-во: {total-1}\n{response_prog}\n")

    # В качестве массива response_prog, массив арифметической прогрессии.
    response_index = elements_index(start=start, finish=finish, elements=response_prog)
    element_value = [v for v in response_prog if response_prog.index(v) in response_index]
    print(f"\nЗадача 32. Индекс элемента\n{'-'*40}\nДиапозон значений: {start} - {finish}\n"
          f"Элементы массива: {element_value}\n"
          f"Индексы элементов: {response_index}\n")


if __name__ == '__main__':
    main()
