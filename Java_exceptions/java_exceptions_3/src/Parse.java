import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Parse {

    public boolean parseData(String[] array) throws ParseException {

        String firstName = array[0];
        String lastName = array[1];
        String patronymic = array[2];

        SimpleDateFormat dateFormat = new SimpleDateFormat("dd.mm.yyyy");
        Date birthdate;
        try {
            birthdate = dateFormat.parse(array[3]);
        } catch (ParseException e) {
            throw new ParseException("Неверный формат даты рождения", e.getErrorOffset());
        }

        int phone;
        try {
            phone = Integer.parseInt(array[4]);
        } catch (NumberFormatException e) {
            throw new NumberFormatException("Неверный формат телефона");
        }

        String gender = array[5];
        if (!gender.toLowerCase().equals("m") && !gender.toLowerCase().equals("f")) {
            throw new RuntimeException("Неверно введен пол");
        }

        System.out.printf("Parse result: %s, %s, %s, %s, %s, %s", lastName, firstName, patronymic, dateFormat.format(birthdate), phone, gender);
        return true;
    }
}
