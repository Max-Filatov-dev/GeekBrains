// Task 41

// Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.

int QuantityPositiveNumbers()
{
    int positiveCount = 0, index = 1;
    Console.WriteLine($"Enter 7 random numbers: \n");

    while (index <= 7)
    {
        Console.Write($"Enter number {index}: ");
        int number = Convert.ToInt32(Console.ReadLine());
        if (number > 0) positiveCount++;
        index++;
    }
    return positiveCount;
}

// Console.WriteLine($"\nQuantity positive numbers: {QuantityPositiveNumbers()}\n");


// Task 43

// Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.

void IntersectionPoint(double k1, double b1, double k2, double b2)
{ 
    double x = (b1 - b2) / (k2 - k1); 
    double y = (k2 * b1 - k1 * b2) / (k2 - k1); 
    if (k1 == k2) Console.Write("Прямые не пересекаются!"); 
    else Console.WriteLine($"\nТочка пересечения: x = {Math.Round(x, 2)}, y = {Math.Round(y, 2)}\n"); 
}

Console.Write("Input b1: "); 
double b1 = Convert.ToDouble(Console.ReadLine()); 
Console.Write("Input k1: "); 
double k1 = Convert.ToDouble(Console.ReadLine()); 
Console.Write("Input b2: "); 
double b2 = Convert.ToDouble(Console.ReadLine()); 
Console.Write("Input k2: "); 
double k2 = Convert.ToDouble(Console.ReadLine()); 

IntersectionPoint(k1, b1, k2, b2);