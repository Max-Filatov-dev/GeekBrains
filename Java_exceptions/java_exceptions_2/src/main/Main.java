package main;

//import main.lesson2.Lesson2;
import main.homework.HomeWork;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

//        Lesson2 lesson2 = new Lesson2();
//        lesson2.wordVerification();

        HomeWork homeWork = new HomeWork();

        // Homework task 1
        System.out.println("Lesson 2 Task 1");
        System.out.println("Вы ввели: " + homeWork.inputNumber());

        // Homework task 2
        System.out.println("\nLesson 2 Task 2");
        homeWork.correctingCode();

        // Homework task 3
        System.out.println("\nLesson 2 Task 3");
        homeWork.correctingCodeSecond();

        // Homework task 4
        System.out.println("\nLesson 2 Task 4");
        System.out.println("Вы ввели: " + homeWork.emptyLine());

    }


}

