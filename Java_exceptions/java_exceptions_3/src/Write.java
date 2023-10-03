import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

public class Write {

    public void writeData(String[] data) {

        String filePath = "/Volumes/DATA/Development/GeekBrains/Java_exceptions/java_exceptions_3/src/files/" + data[0] + ".txt";

        try {
            FileWriter writer = new FileWriter(filePath, true);
            writer.write(Arrays.toString(data) + "\n");
            writer.close();

        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}


