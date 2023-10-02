package main.homework;

import java.util.Locale;
import java.util.Scanner;

public class HomeWork {

    Scanner scanner = new Scanner(System.in);

    /**
     * Lesson 2 Task 1
     *
     * @return Float number
     */
    public float inputNumber() {

//        float number = scanner.nextFloat();
        float number = 0;
        boolean validNumber = false;

        while (!validNumber) {
            scanner.useLocale(Locale.US);
            System.out.print("Введите дробное число: ");
            if (!scanner.hasNextFloat()) {
                System.out.println("Не корректные данные!\n");
            } else {
                number = scanner.nextFloat();
                validNumber = true;
                scanner.nextLine();
            }
        }
        return number;
    }

    /**
     * Lesson 2 Task 2
     */
    public void correctingCode() {

        try {
            int d = 0;
            int[] intArray = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
            double catchedRes = intArray[8] / d;
            System.out.println("catchedRes = " + catchedRes);
        } catch (ArithmeticException e) {
            System.out.println("Catching exception: " + e);
        }
    }

    /**
     * Lesson 2 Task 3
     */
    public void correctingCodeSecond() {

        try {
            int a = 90;
            int b = 3;
            System.out.printf("Division: %d / %d = %d\n", a, b, a / b);
            printSum(23, 234);
            int[] abc = {1, 2};
            abc[3] = 9;
        } catch (ArithmeticException ex) {
            System.out.println(ex);
        } catch (NullPointerException ex) {
            System.out.println("Указатель не может указывать на null!");
        } catch (IndexOutOfBoundsException ex) {
            System.out.println("Массив выходит за пределы своего размера!");
        } catch (Exception ex) {
            System.out.println("Что-то пошло не так..." + ex);
        }
    }

    public void printSum(Integer a, Integer b) {
        System.out.printf("Sum: %d + %d = %d\n", a, b, a + b);
    }

    /**
     * Lesson 2 Task 4
     */
    public void emptyLine() {

        System.out.print("Введите произвольную строку: ");
        String line = scanner.nextLine();

        if (line.isEmpty()) throw new RuntimeException("Пустые строки вводить нельзя!\n");
        else System.out.printf("Вы ввели: %s\n", line);
        scanner.close();
    }

}
