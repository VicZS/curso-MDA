public abstract class Character {
    private WeaponBehavior weapon;
    public Character(WeaponBehavior weapon){
        this.weapon = weapon;
    }
    public void fight(){
        weapon.useWeapon();
    }
    public void setWeapon(WeaponBehavior weapon){
        this.weapon = weapon;
    }

    public void showCharacter(){
        display();
        fight();
    }

    public abstract void display();
}
