// Task 2

// Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.

// Console.Write("Input a first number: ");
// int firstNum = Convert.ToInt32(Console.ReadLine());
// Console.Write("Input a second number: ");
// int secondNum = Convert.ToInt32(Console.ReadLine());

// if (firstNum > secondNum) 
//     Console.WriteLine("First number greater second!");
// else 
//     Console.WriteLine("Second number greater first!");



// Task 4

// Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

// Console.Write("Input a first number: ");
// int numFirst = Convert.ToInt32(Console.ReadLine());
// Console.Write("Input a second number: ");
// int numSecond = Convert.ToInt32(Console.ReadLine());
// Console.Write("Input a third number: ");
// int numThree = Convert.ToInt32(Console.ReadLine());

// int maxNum = numFirst;

// if (numSecond > maxNum)
//     maxNum = numSecond;
// if (numThree > maxNum)
//     maxNum = numThree;
// Console.WriteLine($"Largest number: {maxNum}");



// Task 6

// Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).

// Console.Write("Input number: ");
// int num = Convert.ToInt32(Console.ReadLine());

// if (num % 2 == 0)
//     Console.WriteLine($"Number {num} is even");
// else
//     Console.WriteLine($"Number {num} is odd");


// Task 8

// Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

Console.Write("Input number: ");
int num = Convert.ToInt32(Console.ReadLine());

int current = 0;

while (current <= num)
{
    if (current % 2 == 0)
        Console.Write(current + " ");
    current++;
}