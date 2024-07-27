package Properties;

public class PetrolCars extends ClassicCars{
    
    public PetrolCars(String color,int year,boolean forRent,double Rent) {
        super(color, year, forRent, Rent);
    }
    public PetrolCars(String color,int year,boolean forRent) {
        super(color, year, forRent);
    }
    public PetrolCars(PetrolCars copyPetrolCar) {
        super(copyPetrolCar);
    }
}