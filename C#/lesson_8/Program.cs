// Task 54

Console.WriteLine("\nЗадайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.\n");

int[,] defaultArray = new int[5, 4]
{
    {2,5,9,3}, {6,5,3,7}, {7,9,8,2}, {5,1,6,2}, {8,4,5,7}
};

void ShowArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
            Console.Write(array[i, j] + " ");

        Console.WriteLine();
    }
    Console.WriteLine();
}


int[,] SortArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
        for (int j = 0; j < array.GetLength(1); j++)
            for (int n = 0; n < array.GetLength(1) - 1; n++)
                if (array[i, n] < array[i, n + 1])
                {
                    int temp = array[i, n + 1];
                    array[i, n + 1] = array[i, n];
                    array[i, n] = temp;
                }
    return array;
}

Console.WriteLine("Default massive\n");
ShowArray(array: defaultArray);
Console.WriteLine("Sorted massive\n");
int[,] responseSortArray = SortArray(array: defaultArray);
ShowArray(array: responseSortArray);


// Task 56

Console.WriteLine("\nЗадайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.\n");

void SumLineElements(int[,] array)
{
    int sumLine = int.MaxValue, index = 0;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        int currentLineSum = 0;
        for (int j = 0; j < array.GetLength(1); j++)
            currentLineSum += array[i, j];
        if (currentLineSum < sumLine)
        {
            sumLine = currentLineSum;
            index = i;
        }

    }
    Console.WriteLine($"Наименьшая сумма элементов = {sumLine}, соответсвует строке: {index}\n");
}

SumLineElements(array: defaultArray);