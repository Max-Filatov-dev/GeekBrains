package ru.geekbrains.lesson1;

public class Chocolate extends Product {
    private int weight; // Вес

    public Chocolate(String name, String brand, double price, int weight) {
        super(name, brand, price);
        this.weight = weight;
    }

    public int getWeight() { return weight; }

    @Override
    public String displayInfo() {
        return String.format("[Шоколад] %s - %s - price: %.2f - weight: %d", name, brand, price, weight);
    }

}
