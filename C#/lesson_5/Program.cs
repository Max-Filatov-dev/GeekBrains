// Task 34

// Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.

int[] FillArrayInt()
{
    int[] array = new int[10];
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = new Random().Next(100, 500);
        Console.Write($"{array[i]} ");
    }
    return array;
}


int QuantityEvenNumber(int[] array)
{
    int countEven = 0;
    for (int i = 0; i < array.Length; i++)
        if (array[i] % 2 == 0) countEven++;
    return countEven;
}

// int[] response = FillArrayInt();
// Console.WriteLine($"\n\nQuantity of even numbers: {QuantityEvenNumber(response)}\n");


// Task 36

// Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.

int SumELements(int[] array)
{
    int sum = 0;
    for (int i = 1; i < array.Length; i += 2)
        sum += array[i];
    return sum;
}

// int[] response = FillArrayInt();
// Console.WriteLine($"\n\nSum of odd elements: {SumELements(response)}\n");



// Task 38

// Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.

double[] FillArrayDouble()
{

    double[] array = new double[10];

    Random random = new Random();
    int min = 100;
    int max = 500;

    for (int i = 0; i < 10; i++)
    {
        array[i] = random.NextDouble() * (max - min) + min;
        Console.Write($"{Math.Round(array[i], 2)}, ");
    }
    return array;
}

double FindDifference(double[] array)
{
    double max = array[0];
    double min = array[0];

    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > max) max = array[i];
        else if (array[i] < min) min = array[i];
    }
    return max - min;
}

double[] response = FillArrayDouble();
Console.WriteLine($"\n\nDifference between max and min: {Math.Round(FindDifference(response), 2)}\n");

