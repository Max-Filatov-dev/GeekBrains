
public class Main {
    public static void main(String[] args) {

        Input input = new Input();
        String[] array = input.getData();
        Parse parse = new Parse();
        boolean responseParse = parse.parseData(array);
        if (responseParse) {
            Write write = new Write();
            write.writeData(array);
        }

        Read read = new Read();
        read.readData("Filatov");

    }
}