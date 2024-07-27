package Properties;

public abstract class ClassicCars extends Cars{

    public ClassicCars(String color,int year,boolean forRent,double Rent) {  
        super(color, year, forRent, Rent);
        }

    public ClassicCars (String color,int year,boolean forRent) {
        super(color, year, forRent);
    }
    public ClassicCars (ClassicCars classicCar) {
        super(classicCar);
    }
}
