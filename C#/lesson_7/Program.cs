// Task 47

Console.WriteLine("\nЗадайте двумерный массив размером m×n, заполненный случайными вещественными числами.\n");

double[,] CreateArray(int rows, int columns, double min, double max)
{
    double[,] array = new double[rows, columns];
    Console.WriteLine($"Massive: Rows = {rows} Columns = {columns}\n");
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            array[i, j] = new Random().NextDouble() * (max - min) + min;

    return array;
}

void ShowArray(double[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write(Math.Round(array[i, j], 2) + " ");

        Console.WriteLine();
    }
    Console.WriteLine();
}

double[,] response = CreateArray(rows: 5, columns: 4, min: 10.0, max: 50.0);
ShowArray(array: response);


// Task 50

Console.WriteLine("\nНапишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.");

double ShowElement(int posRow, int posColumn)
{
    int numberRows = response.GetLength(0);
    int numberColumns = response.GetLength(1);

    if (posRow < 0 || posColumn < 0) return 0;
    else if (posRow < numberRows && posColumn < numberColumns) return response[posRow, posColumn];
    else return 0;
}


Console.Write("\nEnter row number: ");
int currentRow = Convert.ToInt32(Console.ReadLine());
Console.Write("Enter column number: ");
int currentColumn = Convert.ToInt32(Console.ReadLine());

double responseShow = Math.Round(ShowElement(posRow: currentRow, posColumn: currentColumn), 2);

if (responseShow != 0) Console.WriteLine($"\nElement value: {responseShow}\n");
else
    Console.WriteLine($"\nElement, Row: {currentRow} and Column: {currentColumn}, in array does not exist!\n");


// Task 52

Console.WriteLine("\nЗадайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов в каждом столбце.\n");

// Павел, я не стал копипастить Task 47, создание двумерного с вещественными числами, в текущий Task, разница лишь в типе данных при создании массива.

void ShowAverage(double[,] array)
{

    for (int i = 0; i < array.GetLength(1); i++)
    {
        int numberRows = response.GetLength(0);
        double sumElement = 0;

        for (int j = 0; j < array.GetLength(0); j++)
            sumElement += array[j, i];
        Console.WriteLine($"Average column {i}: {(sumElement / numberRows):F2}");
    }
    Console.WriteLine();
}

ShowAverage(array: response);