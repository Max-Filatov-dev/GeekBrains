from random import randint

"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""
def exponent_of_number(*, number: int, degree: int) -> int:
    """ """
    return number * exponent_of_number(number=number, degree=degree - 1) if degree > 1 else number


"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def sum_numbers(*, first: int, second: int):
    """ """
    return sum_numbers(first=first+1, second=second-1) if second > 0 else first


def main():
    """ """
    first_number, second_number = randint(2, 10), randint(2, 10)

    print(f"\nЗадача 26. Возведение в степнь\n{'-'*40}\n"
          f"Степень числа: {first_number} ** {second_number} -> {exponent_of_number(number=first_number, degree=second_number):_}\n")

    print(f"\nЗадача 28. Сумма двух чисел\n{'-'*40}\n"
          f"Сумма чисел: {first_number} + {second_number} = {sum_numbers(first=first_number, second=second_number):_}\n")


if __name__ == '__main__':
    main()
