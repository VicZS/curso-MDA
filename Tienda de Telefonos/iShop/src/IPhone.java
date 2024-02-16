public class IPhone extends Product {
    private String model;

    public IPhone(String productName, double price, String model) {
        super(productName, price);
        this.model = model;
    }
}
