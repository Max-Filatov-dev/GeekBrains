// Task 19

// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.

bool PolindromNumber()
{
    int num, rem, sum = 0, temp;
    Console.Write("Enter a number: ");
    num = Convert.ToInt32(Console.ReadLine());
    temp = num;
    while (num > 0)
    {
        rem = num % 10;
        Console.WriteLine($"rem: {rem}");
        num = num / 10;
        Console.WriteLine($"num: {num}");
        sum = sum * 10 + rem;
        Console.WriteLine($"sum: {sum}");
    }
    if (temp == sum)
        return true;
    else
        return false;
}

if (PolindromNumber())
    Console.WriteLine("\nNumber is Palindrome\n");
else
    Console.WriteLine("\nNumber is not a palindrome\n");