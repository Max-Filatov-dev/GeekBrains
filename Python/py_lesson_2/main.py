from random import randint

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


def min_monets():
    """ """
    reshka, orel, total_coins = 0, 0, 15

    for _ in range(total_coins):
        item = randint(1, total_coins)
        if item % 2 == 0:
            reshka += 1
        else:
            orel += 1

    print(f"\nTask_10\n\nReshka: {reshka}, Orel: {orel}\n{'-'*20}\nSmallest: {reshka if reshka <= orel else orel}\n")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


def random_number():
    """ """
    rand_x, rand_y = randint(1, 1000), randint(1, 1000)
    number_x, number_y = None, None

    print(f"\nTask_12\n\nrand_x: {rand_x} rand_y: {rand_y}\n{'-'*30}")
    for x in range(rand_x):
        for y in range(rand_y):
            if x + y == rand_x:
                number_x = x + y
            elif x * y == rand_y:
                number_y = x * y

    print(f"Num_x: {number_x} Num_y: {number_y}\n")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def integer_powers():
    """ """
    rand_int, count, int_pow = randint(1, 20), 0, 0
    print(f"\nTask_14\n{'-'*20}\nrand_int: {rand_int}\n")

    while int_pow <= rand_int:
        print(int_pow)
        count += 1
        int_pow = 2 ** count


def main():
    min_monets()
    random_number()
    integer_powers()


if __name__ == '__main__':
    main()