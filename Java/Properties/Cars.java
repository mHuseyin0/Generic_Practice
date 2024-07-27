package Properties;
import java.util.ArrayList;

public abstract class Cars implements Vehicles { 
    public String color;
    public int year;
    public boolean forRent;
    public double Rent;
    public boolean engineWorking = false;
    public boolean isGoing = false;
    public int carNum;
    public static int carsNum = 0;

    public static ArrayList<Object> rentables = new ArrayList<>();
    public static ArrayList<Object> myCarsOutGarage = new ArrayList<>();
    public static ArrayList<Object> allMyCars = new ArrayList<>();

    public static void getInfo (Object memoryLocation) {
        
    }

    public Cars (String color,int year,boolean forRent,double Rent) {
        this.color = color;
        this.year = year;
        this.forRent = forRent;
        this.Rent = Rent;
        carsNum++;
        this.carNum = carsNum;
        myCarsOutGarage.add(this);
        if (this.forRent == true) {
            rentables.add(this);
        }
        allMyCars.add(this);
    }

    public Cars (String color,int year,boolean forRent) {
        this.color = color;
        this.year = year;
        this.forRent = forRent;
        carsNum++;
        this.carNum = carsNum;
        myCarsOutGarage.add(this);
        if (this.forRent == true) {
            rentables.add(this);
        }
        allMyCars.add(this);
        
    }

    public Cars (Cars copyCar) {
        this.color = copyCar.getColor();
        this.year = copyCar.getYear();
        this.forRent = copyCar.getForRent();
        this.Rent = copyCar.getRent();
    }

    @Override
    public void startEngine() {
        if (this.engineWorking == false) {
            System.out.println();
            System.out.printf("You started the engine of car %d.",this.carNum);
            System.out.println();
            this.engineWorking = true;
        }
        else {
            System.out.println();
            System.out.printf("Car %d:The engine has been working already.",this.carNum);
            System.out.println();
        }
    }
    
    @Override
    public void stopEngine() {
        if (this.engineWorking == true) {
            System.out.println();
            System.out.printf("You stopped the engine of %d.",this.carNum);
            System.out.println();
            this.engineWorking = false;
        }
        else {
            System.out.println();
            System.out.printf("Car %d:The engine has been stopped already.",this.carNum);
            System.out.println();
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
            if (this.engineWorking == false) {
                System.out.printf("Please start the engine of car %d before trying to move.",this.carNum);
                System.out.println();
            } 
            else {
                System.out.println();
                System.out.printf("The car " +this.carNum+ " has started to move.");
                System.out.println();
                this.isGoing = true;
            }
        }
    }
    public String getColor() {
        return color;
    }
    public int getYear() {
        return year;
    }
    public double getRent() {
        return Rent;
    }
    public boolean getForRent() {
        return forRent;
    }
    public void setColor(String color) {
        this.color = color;
    }
    public void setYear(int year) {
        this.year = year;
    }
    public void setForRent(boolean forRent) {
        this.forRent = forRent;
    }
    public void setRent(double rent) {
        Rent = rent;
    }
    public void copyCar(Cars car) {
        setColor(car.getColor());
        setYear(car.getYear());
        setForRent(car.getForRent());
        setRent(car.getRent());
    }
}
