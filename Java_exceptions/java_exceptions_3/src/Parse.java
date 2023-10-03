import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Parse {

    public boolean parseData(String[] array) {

        String lastName = array[0];
        String firstName = array[1];
        String patronymic = array[2];

        SimpleDateFormat dateFormat = new SimpleDateFormat("dd.mm.yyyy");
        Date birthdate = null;
        try {
            birthdate = dateFormat.parse(array[3]);
        } catch (ParseException e) {
            System.out.println("Неверный формат даты рождения" + e.getErrorOffset());
        }

        int phone = 0;
        try {
            phone = Integer.parseInt(array[4]);
        } catch (NumberFormatException e) {
            e.printStackTrace();
        }

        String gender = array[5];
        if (!gender.toLowerCase().equals("m") && !gender.toLowerCase().equals("f")) {
            throw new RuntimeException("Неверно введен пол");
        }

        System.out.printf("\nParse result: %s, %s, %s, %s, %s, %s\n", lastName, firstName, patronymic, dateFormat.format(birthdate), phone, gender);
        return true;
    }
}
