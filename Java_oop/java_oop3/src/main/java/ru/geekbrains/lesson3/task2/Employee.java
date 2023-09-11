package ru.geekbrains.lesson3.task2;

/**
 * Работник
 */
public abstract class Employee implements Comparable<Employee> {

    /**
     * Имя
     */
    protected String name;

    /**
     * Фамилия
     */
    protected String surName;

    /**
     * Возраст
     */
    protected int age;

    /**
     * Ставка заработной платы
     */
    protected double salary;

    /**
     * Расчет среднемесячной заработной платы
     *
     * @return
     */
    public abstract double calculateSalary();
    public abstract int ageSort();


    public Employee(String name, String surName, int age, double salary) {
        this.name = name;
        this.surName = surName;
        this.age = age;
        this.salary = salary;
    }

    @Override
    public String toString() {
        return String.format("%s %s", surName, name);
    }

    @Override
    public int compareTo(Employee o) {
        int surNameRes = surName.compareTo(o.surName);
        if (surNameRes == 0) {
            return name.compareTo(o.name);
        }
        return surNameRes;

//        int ageRes = age.compareTo(o.age);
//        if (ageRes == 0) {
//            return age.compareTo(o.age);
//        }
//        return ageRes;
    }
}
