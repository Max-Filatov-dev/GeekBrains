// Task 64

Console.WriteLine("\nTask 64\nЗадайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии.\n");

int valueM = 2;
int valueN = 5;

Console.WriteLine($"Значение N: {valueN}\n");

void ShowNum(int num)
{
    Console.Write(num + " ");
    if (num > 1) ShowNum(num - 1);
}

ShowNum(num: valueN);


// Task 66

Console.WriteLine("\n\n\nTask 66\nЗадайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.\n");

Console.WriteLine($"Значение M: {valueM}\nЗначение N: {valueN}\n");

int SumOfDigits(int m, int n)
{
    if (m > n || m <= 0) return 0;
    else if (m == n) return m;
    else return n + SumOfDigits(m, n - 1);
}

int responseSum = SumOfDigits(m: valueM, n: valueN);
if (responseSum == 0 || responseSum == valueM) Console.WriteLine($"Не корректные данные!\nУсловия: M > 0 и N > M");
else
    Console.WriteLine($"Cумма натуральных элементов: {responseSum}");


// Task 68

Console.WriteLine("\n\nTask 68\nНапишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.\n");

int Akkerman(int m, int n)
{
    if (m < 0 || n < 0) return 0;
    else if (m == 0) return n + 1;
    else if (n == 0 && m > 0) return Akkerman(m - 1, 1);
    else return (Akkerman(m - 1, Akkerman(m, n - 1)));
}

int responseAker = Akkerman(m: valueM, n: valueN);
if (responseAker == 0) Console.WriteLine($"Не корректные данные!\nУсловия: M > 0 и N > 0");
else
    Console.WriteLine($"Результат функции Аккермана: {responseAker}\n");