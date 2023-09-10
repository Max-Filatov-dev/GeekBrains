public class Main {

    public static void main(String[] args) {
        Plate plate = new Plate(100);

        // One cat
        /*
        Cat cat = new Cat("Barsik", 20, false);
        int response = cat.eat(plate.getFood());
        plate.setFood(response);
        if (cat.isSatiety()) {
            System.out.printf("Котейка %s наелся. :)\n", cat.getName());
            plate.info();
        }
        */

        // All cats
        Cat[] cats = new Cat[3];
        cats[0] = new Cat("Kuzya", 50, false);
        cats[1] = new Cat("Barsik", 40, false);
        cats[2] = new Cat("Yashka", 30, false);

        for (var item : cats) {
            int response = item.eat(plate.getFood());
            plate.setFood(response);
            if (item.isSatiety()) {
                System.out.printf("Котейка %s наелся. :)\n", item.getName());
                plate.info();
            }
        }
        // Добавить в тарелку еды.
        plate.setFood(100);
//        plate.info();
    }
}
