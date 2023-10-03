import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Read {

    public void readData(String name) {

        String filePath = "/Volumes/DATA/Development/GeekBrains/Java_exceptions/java_exceptions_3/src/files/" + name + ".txt";

        try {
            FileReader reader = new FileReader(filePath);
            System.out.printf("\nRead file: %s\n", name);
            int i;
            while ((i = reader.read()) != -1)
                System.out.print((char) i);
            reader.close();
        } catch (FileNotFoundException nt) {
            nt.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        }

    }
}
