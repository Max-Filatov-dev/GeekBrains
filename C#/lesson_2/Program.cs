// Task 10

// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

int CutNumber(int num)
{
    return num / 10 % 10;
}

Console.WriteLine($"Second digit: {CutNumber(num: 357)}");


// Task 13

// Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

void ThirdDigit(int num)
{
    if (num < 100) Console.WriteLine($"The number {num} is not three digits!");
    else
    {
        while (num > 999)
    {
        // цикл делит num до трехзначного числа
        num /= 10;
        // Console.WriteLine(num);
    }
    Console.WriteLine($"Third digit: {num % 10}");
    }
}

ThirdDigit(num: 3579321);


// Task 15

// Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


bool DayOff(int numDay)
{
    if (numDay <= 0 || numDay > 7)
    {
        Console.WriteLine($"Invalid number: {numDay}, Input 1 of 7");
        return false;
    }
    else if (numDay < 6)
    {
        Console.WriteLine("Today is a working day :(");
        return false;
    }
    else return true;

}

if (DayOff(numDay: 5)) Console.WriteLine("Today is a day off :)");