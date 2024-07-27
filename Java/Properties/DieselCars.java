package Properties;

public class DieselCars extends ClassicCars{
    
    public DieselCars(String color,int year,boolean forRent,double Rent) {
        super(color, year, forRent, Rent);
    }
    public DieselCars(String color,int year,boolean forRent) {
        super(color, year, forRent);
    }
    public DieselCars(DieselCars copyDieselCar) {
        super(copyDieselCar);
    }
}
