// Task 19

// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.

bool PolindromNumber()
{
    int number, remineder, temp, total = 0;
    Console.Write("Enter a number: ");
    number = Convert.ToInt32(Console.ReadLine());
    temp = number;
    while (number > 0)
    {
        remineder = number % 10;
        number /= 10;
        total = total * 10 + remineder;
    }
    if (temp == total)
        return true;
    else
        return false;
}
/*
if (PolindromNumber())
    Console.WriteLine("\nNumber is Palindrome\n");
else
    Console.WriteLine("\nNumber is not a palindrome\n");
*/



// Task 21

// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

double GetDistance(double x1, double y1, double z1, double x2, double y2, double z2)
{
    double distance = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2) + Math.Pow(z2 - z1, 2));
    return distance;
}

// Тип var -> неизвестно, что введет пользователь. Возможно int (5), возможно double (5,37)
/*
Console.Write("Введите координаты x1: ");
var firstX = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите координаты y1: ");
var firstY = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите координаты z1: ");
var firstZ = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите координаты x2: ");
var secondX = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите координаты y2: ");
var secondY = Convert.ToDouble(Console.ReadLine());
Console.Write("Введите координаты z2: ");
var secondZ = Convert.ToDouble(Console.ReadLine());

double response = GetDistance(x1: firstX, y1: firstY, z1: firstZ, x2: secondX, y2: secondY, z2: secondZ);
Console.WriteLine($"Distance between two points = {Math.Round(response, 2)}");
*/



// Task 23

// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

void TableCube(int number)
{
    for (int i = 0; i <= number; i++)
    {
        for (int j = 1; j <= number; j++)
        {
            double numberCube = Math.Pow(j, 3);
            Console.Write($"{numberCube}, ");
        }
        Console.WriteLine();
    }
}
/*
Console.Write("Input number: ");
int number = Convert.ToInt32(Console.ReadLine());
TableCube(number: number);
*/