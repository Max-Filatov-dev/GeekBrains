// Task 34

// Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.

int[] array = new int[10];
for (int i = 0; i < array.Length; i++)
{
    array[i] = new Random().Next(100, 500);
    Console.Write($"{array[i]} ");
}

int QuantityEvenNumber()
{
    int countEven = 0;
    for (int i = 0; i < array.Length; i++)
        if (array[i] % 2 == 0) countEven++;
    return countEven;
}

Console.WriteLine($"\n\nQuantity of even numbers: {QuantityEvenNumber()}\n");