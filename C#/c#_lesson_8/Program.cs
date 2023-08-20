// Task 54

Console.WriteLine("\nЗадайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.\n");

int[,] initialArray = new int[4, 4]
{
    {2,5,9,1},
    {8,4,3,7},
    {5,4,2,3},
    {7,3,1,5}
};

void Show2DArray(int[,] array2D)
{
    for (int i = 0; i < array2D.GetLength(0); i++)
    {
        for (int j = 0; j < array2D.GetLength(1); j++)
            Console.Write(array2D[i, j] + " ");

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

Console.WriteLine("Initial massive\n");
Show2DArray(array2D: initialArray);
Console.WriteLine("Sorted massive\n");
int[,] responseSortArray = SortArray(array: initialArray);
Show2DArray(array2D: responseSortArray);


// Task 56

Console.WriteLine("\nЗадайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.\n");

Show2DArray(array2D: initialArray);

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
    Console.WriteLine($"Строка с наименьшей суммой элементов: {index}, Сумма элементов: {sumLine}\n");
}
SumLineElements(array: initialArray);


// Task 58

Console.WriteLine("\nЗадайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.\n(Чтобы можно было умножить две матрицы, количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!)\n");

int[,] firstMatrix = new int[3, 4]
{
    {7,9,6,5},
    {5,5,1,4},
    {3,8,4,7},
};
int[,] secondMatrix = new int[4, 3]
{
    {4,2,5},
    {3,1,7},
    {9,5,3},
    {1,7,4}
};

Console.WriteLine("First matrix\n");
Show2DArray(array2D: firstMatrix);
Console.WriteLine("Second matrix\n");
Show2DArray(array2D: secondMatrix);

int[,] MatrixProduct(int[,] firstMat, int[,] secondMat)
{
    int[,] resultMatrix = new int[firstMat.GetLength(0), secondMat.GetLength(1)];
    for (int i = 0; i < resultMatrix.GetLength(0); i++)
        for (int j = 0; j < resultMatrix.GetLength(1); j++)
        {
            int sum = 0;
            for (int k = 0; k < firstMat.GetLength(1); k++)
                sum += firstMat[i, k] * secondMat[k, j];
            resultMatrix[i, j] = sum;
        }
    return resultMatrix;
}


int[,] responseMatProduct = MatrixProduct(firstMat: firstMatrix, secondMat: secondMatrix);
Console.WriteLine("Result:\n");
Show2DArray(array2D: responseMatProduct);


// Task 60

Console.WriteLine("\nСформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.\n");

int[,,] Create3DArray()
{
    int[,,] array3D = new int[3, 3, 3];
    int firstNumber = 10;

    for (int i = 0; i < array3D.GetLength(0); i++)
        for (int j = 0; j < array3D.GetLength(1); j++)
            for (int k = 0; k < array3D.GetLength(2); k++)
            {
                if (firstNumber >= 100)
                    break;
                else array3D[i, j, k] = firstNumber += 2;
            }

    return array3D;
}

void Show3DArray(int[,,] array3D)
{
    for (int i = 0; i < array3D.GetLength(0); i++)
        for (int j = 0; j < array3D.GetLength(1); j++)
        {
            for (int k = 0; k < array3D.GetLength(2); k++)
                Console.Write($"{array3D[i, j, k]}({i},{j},{k}) ");

            Console.WriteLine();
        }
    Console.WriteLine();
}

int[,,] response3D = Create3DArray();
Show3DArray(array3D: response3D);


// Task 62

Console.WriteLine("\nНапишите программу, которая заполнит спирально массив 4 на 4.\n");

int[,] Spiral(int n)
{
    int[,] result = new int[n, n];

    int pos = 1;
    int count = n;
    int value = -n;
    int sum = -1;

    do
    {
        value = -1 * value / n;
        for (int i = 0; i < count; i++)
        {
            sum += value;
            result[sum / n, sum % n] = pos++;
        }
        value *= n;
        count--;
        for (int i = 0; i < count; i++)
        {
            sum += value;
            result[sum / n, sum % n] = pos++;
        }
    } while (count > 0);

    return result;
}

void ShowSpiral(int[,] array)
{
    int n = (array.GetLength(0) * array.GetLength(1) - 1).ToString().Length + 1;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (array[i, j] < 10) Console.Write($"0{array[i, j]}");
            else Console.Write(array[i, j]);
            Console.Write(" ");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
}

int[,] responseSpiral = Spiral(n: 4);
ShowSpiral(array: responseSpiral);