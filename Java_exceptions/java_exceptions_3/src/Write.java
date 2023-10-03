import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

public class Write {

    public void writeData(String[] data) {

        try {
            FileWriter writer = new FileWriter(data[0], true);
            writer.write(Arrays.toString(data) + "\n");
            writer.close();

        } catch (IOException ex) {
            System.out.println(ex.getStackTrace());
        }
    }
}


