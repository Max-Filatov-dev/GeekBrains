package ru.geekbrains.lesson3.task2;

import java.util.Arrays;
import java.util.Random;

public class Program {

    private static Random random = new Random();

    /**
     * TODO: Переработать метод generateWorker. Метод должен возвращать случайного
     *  сотрудника (Freelancer или Worker)
     *
     * @return
     */
//    public static Worker generateWorker() {
    public static Employee generateEmployee() {
        String[] names = new String[]{"Анатолий", "Глеб", "Клим", "Мартин", "Лазарь", "Владлен", "Клим", "Панкратий", "Рубен", "Герман"};
        String[] surNames = new String[]{"Григорьев", "Фокин", "Шестаков", "Хохлов", "Шубин", "Бирюков", "Копылов", "Горбунов", "Лыткин", "Соколов"};

        int ageNumber = random.nextInt(25, 55);
        int salaryIndex = random.nextInt(200, 500);

        if (random.nextBoolean()) {
            return new Worker(names[random.nextInt(names.length)], surNames[random.nextInt(surNames.length)], ageNumber,
                    100 * salaryIndex);
        } else {
            return new Freelancer(names[random.nextInt(names.length)], surNames[random.nextInt(surNames.length)], ageNumber,
                    100 * salaryIndex);
        }

    }

    public static Employee[] generateEmployees(int count) {
        Employee[] employees = new Employee[count];
        for (int i = 0; i < count; i++) {
            employees[i] = generateEmployee();
        }
        return employees;
    }

    public static void main(String[] args) {
        Employee[] employees = generateEmployees(12);

//        for (Employee employee : employees) {
//            System.out.println(employee);
//        }

        Arrays.sort(employees, new AgeComparator());
        System.out.println();

        for (Employee employee : employees) {
            System.out.println(employee);
        }

    }

}
