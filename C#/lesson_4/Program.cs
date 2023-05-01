// Task 25

//  Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.

int NumberExponent(int number, int exponent)
{
    int result = 1;
    for (int i = 0; i < exponent; i++)
    {
        result *= number;
    }
    return result;
}
/*
Console.Write("Input a number: ");
int number = Convert.ToInt32(Console.ReadLine());
Console.Write("Enter exponent: ");
int exponent = Convert.ToInt32(Console.ReadLine());

int response = NumberExponent(number: number, exponent: exponent);
Console.WriteLine($"\nNumber {number} to the power of {exponent} = {response}\n");
*/



// Task 27

// Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.

int SumNumber(int number)
{
    int sum = 0;
    while (number > 0)
    {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}

// Console.Write("Input a random number: ");
// int number = Convert.ToInt32(Console.ReadLine());
// int response = SumNumber(number: number);
// Console.WriteLine($"\nSum of digits {number} = {response}\n");



// Task 29

// Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.

void FillArray()
{
    int[] array = new int[8];
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(1, 100);
        Console.Write($"{array[i]} ");
    }
}

FillArray();