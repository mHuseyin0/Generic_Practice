package Properties;

public class FlyingCars extends Cars implements AirPlanes {

    public int numWings;
    public int numRotors;
    public boolean isInSky = false;

    public FlyingCars(String color,int year,boolean forRent,double Rent,int numRotors,int numWings) {
        super(color,year,forRent,Rent);
        this.numRotors = numRotors;
        this.numWings = numWings;
    }

    public FlyingCars(String color,int year,boolean forRent,int numRotors,int numWings) {
        super(color,year,forRent);
        this.numRotors = numRotors;
        this.numWings = numWings;
    }
    public FlyingCars(FlyingCars copyFlyingCar) {
        super(copyFlyingCar);
        this.numRotors = copyFlyingCar.getNumRotors();
        this.numWings = copyFlyingCar.getNumWings();
    }
    @Override
    public void raise() {
        if (this.isInSky == true) {
            System.out.println();
            System.out.printf(this.carNum+ " is already at the sky.");
            System.out.println();
        }
        else {
            if (this.engineWorking == false) {
                System.out.println("Please start the engine of car " +this.carNum+ " before trying to fly.");
            } 
            else {
                System.out.println();
                System.out.printf("Car " + this.carNum + " has raised to the sky.");
                System.out.println();
                this.isInSky = true;
            }   
        }
    }

    @Override
    public void go() {
        if (this.isGoing == true) {
            System.out.println();
            System.out.printf("The car " +this.carNum+ " is already going.");
            System.out.println();
        }
        else {
            if (this.engineWorking == false || this.isInSky == false) {
                System.out.println();
                System.out.println("Please make sure that you started the engine and raised car " + this.carNum + " before trying to move.");
            } 
            else {
                System.out.println();
                System.out.printf("Car " +this.carNum+ " has started to move.");
                System.out.println();
                this.isGoing = true;
            }
        }
    }
    public int getNumRotors() {
        return numRotors;
    }
    public int getNumWings() {
        return numWings;
    }
    public void setNumRotors(int numRotors) {
        this.numRotors = numRotors;
    }
    public void setNumWings(int numWings) {
        this.numWings = numWings;
    }
    
    public void copyCar(FlyingCars car) {
        setColor(car.getColor());
        setYear(car.getYear());
        setForRent(car.getForRent());
        setRent(car.getRent());
        setNumRotors(car.getNumRotors());
        setNumWings(car.getNumWings());
    }
}
