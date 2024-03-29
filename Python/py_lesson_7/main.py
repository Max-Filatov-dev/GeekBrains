"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке 
"""


def ritm_in_phrase():
    """ """
    phrase = input('Введите фразу (пара-ра-рам...): ').split()
    count = list(map(lambda x: x.count('а'), phrase))
    print('Ритм: Парам пам-пам\n') if len(set(count)) == 1 else print('Нет ритма: Пам парам\n')


"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
"""


def print_operation_table(operation, num_rows=6, num_columns=6):
    """ """
    # заполяем фукцией operation вложенный массив [[], []]
    numbers = [[operation(i, j) for j in range(1, num_columns+1)] for i in range(1, num_rows+1)]
    return list(map(lambda x: print(*x) , numbers))


def main():
    """ """
    print(f"\nЗадача 34. Ритм в стихах\n{'-'*40}")
    ritm_in_phrase()

    print(f"\nЗадача 36. Элемент по номеру строки и столбца\n{'-'*50}")
    print_operation_table(operation=lambda x, y: x*y)


if __name__ == '__main__':
    main()
