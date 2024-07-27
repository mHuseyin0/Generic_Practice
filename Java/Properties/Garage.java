package Properties;
import java.util.ArrayList;

public class Garage {
    
    public int size;
    public ArrayList<Object> GarageIndex = new ArrayList<>();

    public Garage(int size) {
        this.size = size;
    }

    public void park(Cars car) {
        if (this.GarageIndex.contains(car)) {
            System.out.println(car +" is already in "+ this +".");
        }
        else if (!(Cars.myCarsOutGarage.contains(car))) {
            System.out.println("The "+ car +" is in another garage.");
        }
        else {
            if (this.size == 0) {
                System.out.println("The "+this+" is full.");
            }
            else {
                System.out.println("The "+ car +" has been parked to the "+ this +".");
                this.size-=1;
                System.out.println("Remaining space in this garage: "+this.size);
                this.GarageIndex.add(car);
                Cars.myCarsOutGarage.remove(car);
            }
        }
    }

    public void removeCar(Cars car) {
        if (this.GarageIndex.contains(car)) {
            System.out.println("The "+ car +" has been removed from the "+ this +".");
            this.size+=1;
            System.out.println("Remaining space in this garage: "+this.size);
            this.GarageIndex.remove(car);
            Cars.myCarsOutGarage.add(car);

        }
        else {
            System.out.println("The "+ car + " is not in the "+ this +".");
        }
    }
    
}
