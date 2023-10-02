package main.lesson2;

import java.util.HashMap;

/**
 * Запишите в файл следующие строки:
 * Анна=4
 * Елена=5
 * Марина=6
 * Владимир=?
 * Константин=?
 * Иван=4
 * Реализуйте метод, который считывает данные из файла и сохраняет в двумерный массив (либо HashMap, если студенты с ним знакомы). В отдельном
 * методе нужно будет пройти по структуре данных, если сохранено значение ?, заменить его на соответствующее число. Если на каком-то месте встречается
 * символ, отличный от числа или ?, бросить подходящее исключение.Записать в тот же файл данные с замененными символами ?.
 */

public class Lesson2 {

    public void wordVerification() {

        try {
            HashMap<String, String> name_length = new HashMap<>();
            name_length.put("Анна", "4");
            name_length.put("Елена", "5");
            name_length.put("Марина", "6");
            name_length.put("Владимир", "?");
            name_length.put("Константин", "?");
            name_length.put("Иван", "4");

            for (String key : name_length.keySet()) {
                String value = name_length.get(key);
                if ("?".equals(value)) {
                    name_length.put(key, String.valueOf(key.length()));
                }
            }

            System.out.println(name_length);
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

}
