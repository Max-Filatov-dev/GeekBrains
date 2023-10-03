import java.util.ArrayList;
import java.io.FileWriter;
import java.io.IOException;

public class Write {

    public void writeData(ArrayList arrayList) {

        try {
            FileWriter writer = new FileWriter("notes3.txt", false);
            writer.write(arrayList.iterator().toString());
            writer.close();

        } catch (IOException ex) {
            System.out.println(ex.getStackTrace());
        }
    }
}


