package Properties;
public class ElectricCars extends Cars{

    public ElectricCars(String color,int year,boolean forRent,double Rent) {
        super(color, year, forRent, Rent);
    }

    public ElectricCars(String color,int year,boolean forRent) {
        super(color, year, forRent);
    }

    public ElectricCars(ElectricCars copyElectricCar) {
        super(copyElectricCar);
    }
}