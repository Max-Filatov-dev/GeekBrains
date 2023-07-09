def check_data() -> str:
    while True:
        number = input('\nВведите число: ')
        # Проверка на пустату и отсутствие букв
        if number.isdigit():
            return number
        else:
            print('\nНе корректные данные! (Только натуральное число: N > 0...)\n(Для выхода нажать Ctrl + C)')

# Задача 2: Найдите сумму цифр трехзначного числа.

def sum_number(*, number: int):
    """ """
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    print(f"Сумма цифр: {result}\n{'='*30}\n")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?


def number_of_cranes(*, cranes: int):
    """ """
    # Cranes делим на общее кол-во(3) участников, полученое делим на кол-во(2) парней
    petay = int(cranes / 3 / 2)
    serg = petay
    katya = (petay + serg) * 2
    total = petay + serg + katya
    print(f"\nВместе сделали {total}. Катя сделала: {katya}, Петя и Серега каждый по: {petay}\n{'='*70}\n")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.


def lucky_ticket(*, ticket_number: str):
    """ """
    numbers = [int(i) for i in ticket_number]
    len_numbers = int(len(numbers) / 2)
    if sum(numbers[:len_numbers]) == sum(numbers[len_numbers:]):
        print('Билет счастливый!\n')
    else:
        print('Несчастливый билет...\n')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).


def chocolate(*, n: int, m: int, k: int):
    """ """
    if k < n * m and (k % n == 0 or k % m == 0):
        print('\nМожно рзломить!\n')
    else:
        print('\nНельзя разломить!\n')


# Задача 10: Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.


def leap_year(*, year: int):
    """ """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('\nДа, год високосный!\n')
    else:
        print('\nНет, год невисокосный!\n')


def main():
    """ """
    print(f"\nЗадача 2. (Сумма цифр) Введите натуральное число\n{'-'*40}")
    sum_number(number=int(check_data()))

    print(f"\nЗадача 4. (Кол-во журавликов) Введите натуральное число\n{'-'*40}")
    number_of_cranes(cranes=int(check_data()))

    print(f"\nЗадача 6. (Счастливый билет) Введите номер билета (натуральное число)\n{'-'*40}")
    lucky_ticket(ticket_number=check_data())

    print(f"\nЗадача 8. (Шоколадка) Введите размер шоколадки m x n (дольки) и кол-во k долек (натуральные числа)\n{'-'*40}")
    n_dol = int(check_data())
    m_dol = int(check_data())
    k_dol = int(check_data())
    chocolate(n=n_dol, m=m_dol, k=k_dol)

    print(f"\nЗадача 10. (Високосный год) Введите год (натуральное число)\n{'-'*40}")
    leap_year(year=int(check_data()))


if __name__ == '__main__':
    main()
