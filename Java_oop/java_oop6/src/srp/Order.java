package srp;

public class Order {

    // region Private or Protected Fields

    protected String clientName;
    protected String email;
    protected String product;
    protected int qnt;
    protected double price;

    // endregion

    // region Constructors

    public Order() {
    }

    public Order(String clientName, String email, String product, int qnt, int price) {
        this.clientName = clientName;
        this.email = email;
        this.product = product;
        this.qnt = qnt;
        this.price = price;
    }

    // endregion

    // region Public Getters And Setters (Properties)

    public String getClientName() {
        return clientName;
    }

    public String getEmail() {
        return email;
    }

    public String getProduct() {
        return product;
    }

    public int getQnt() {
        return qnt;
    }

    public double getPrice() {
        return price;
    }

    // endregion

}
