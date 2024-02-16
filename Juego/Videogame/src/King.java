public class King extends Character{
    public King(){
        super(new SwordBehavior());
    }
    public void display(){
        System.out.println("I am a King");
    }
    
}

