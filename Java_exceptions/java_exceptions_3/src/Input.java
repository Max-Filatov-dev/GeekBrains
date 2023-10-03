import java.util.ArrayList;
import java.util.Scanner;

public class Input {

    public String[] getData() {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите фамилию, имя, отчество, дату рождения (в формате dd.mm.yyyy), номер телефона (число без разделителей) и " +
                "пол(символ латиницей f или m), разделенные пробелом");
        String data = scanner.nextLine();
        scanner.close();

        String[] array = data.split(" ");
        if (array.length != 6) throw new RuntimeException("Введено неверное количество параметров");
        return array;
    }

}
