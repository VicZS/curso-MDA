public abstract class Beverage {
    String description = "Unknown Beverage";
    String size = "Small";

    public String getDescription(){
        return description + " - "+ size;
    }

    public void setSize(String size){
        this.size = size;
    }

    public abstract double cost();

    public double costf(){
        double costofinal = cost();
        switch (this.size) {
            case "Medium":
            costofinal *= 1.5;
                break;
            
            case "Large":
            costofinal *= 2;
                break;
            default:
                break;
        }
        return costofinal;
    }

}