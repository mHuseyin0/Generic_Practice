import java.util.HashMap;
import java.util.Scanner;

import Properties.*;

public class Main5_Class {
    public static void main(String[] args) {
        /*
        DieselCars myCar1 = new DieselCars("White",2009,true,400);
        
        PetrolCars myCar2 = new PetrolCars("Light Blue",2020,true,900);
        
        DieselCars myCar3 = new DieselCars("Black",2016,false);
        
        FlyingCars myCar4 = new FlyingCars("Black", 2023, false, 4, 0);
        
        PetrolCars myCar5 = new PetrolCars("Red",2015,false);

        ElectricCars myCar6 = new ElectricCars("Yellow",2022,false);
        
        DieselCars myCar7 = new DieselCars("Light Gray", 2018, true,700);

        Garage myGarage1 = new Garage(5);

        Garage myGarage2 = new Garage(10);
        */
        Scanner myScanner = new Scanner(System.in);

        HashMap<Integer,Object> myCars = new HashMap<>();

        int objNum = 0;
        String inpColor;
        Integer inpYear = null;
        String inpForRent;
        boolean boolForRent = false;
        Double inpRent = null;
        Integer choice; 
        do {
            choice = null;
            System.out.println("\nPlease enter a number to choose which car type do you want to create (Input any other number to quit.):\n1=Petrol Car\n2=Diesel Car\n3=Electric Car\n4=Flying Car\nYour input: ");
            
            do {
                try {
                choice = myScanner.nextInt();
                } catch (Exception e) {
                System.out.println("Please input a number.");
                }
                myScanner.nextLine();
            }while (choice == null);
            


            if (choice == 1) {
                System.out.println("Please enter your car's color:");
                inpColor = myScanner.nextLine();
                do{
                    System.out.println("Please enter the year your car produced:");
                    try{
                        inpYear = myScanner.nextInt();
                    }
                    catch (Exception e) {
                        System.out.println("Please input a number.");
                    }
                    myScanner.nextLine();
                } while (inpYear == null);
                
                do{
                    System.out.println("Please enter whether your car for rent or not (Input Yes or No.):");
                    inpForRent = myScanner.nextLine();
                    if (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No"))) {
                        System.out.println("Please input yes or no.(Capitalization is ignored.)");
                    }
                }while (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No")));
                if (inpForRent.equalsIgnoreCase("Yes")) {
                    boolForRent = true;
                    
                    do{
                        System.out.println("Please enter your car's rent cost.(If it's unknown you can input 0.)");
                        try{
                            inpRent = myScanner.nextDouble();
                            if (inpRent < 0) {
                            System.out.println("Please input a positive number.");
                            }
                        }
                        catch (Exception e) {
                            System.out.println("Please input a number.");
                        }
                        myScanner.nextLine();
                    }while (inpRent == null || inpRent<0);
                }
                if (boolForRent == true && inpRent != 0) {
                    myCars.put(objNum, new PetrolCars(inpColor, inpYear, boolForRent, inpRent));
                }
                else {
                    myCars.put(objNum, new PetrolCars(inpColor, inpYear, boolForRent));
                }
                objNum++;
                inpYear = null;
                inpRent = null;
                boolForRent = false;
            } 



            else if(choice == 2) {
                System.out.println("Please enter your car's color:");
                inpColor = myScanner.nextLine();
                do{
                    System.out.println("Please enter the year your car produced:");
                    try{
                        inpYear = myScanner.nextInt();
                    }
                    catch (Exception e) {
                        System.out.println("Please input a number.");
                    }
                    myScanner.nextLine();
                } while (inpYear == null);
                
                do{
                    System.out.println("Please enter whether your car for rent or not (Input Yes or No.):");
                    inpForRent = myScanner.nextLine();
                    if (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No"))) {
                        System.out.println("Please input yes or no.(Capitalization is ignored.)");
                    }
                }while (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No")));
                if (inpForRent.equalsIgnoreCase("Yes")) {
                    boolForRent = true;
                    
                    do{
                        System.out.println("Please enter your car's rent cost.(If it's unknown you can input 0.)");
                        try{
                            inpRent = myScanner.nextDouble();
                            if (inpRent < 0) {
                            System.out.println("Please input a positive number.");
                            }
                        }
                        catch (Exception e) {
                            System.out.println("Please input a number.");
                        }
                        myScanner.nextLine();
                    }while (inpRent == null || inpRent<0);
                }
                if (boolForRent == true && inpRent != 0) {
                    myCars.put(objNum, new DieselCars(inpColor, inpYear, boolForRent, inpRent));
                }
                else {
                    myCars.put(objNum, new DieselCars(inpColor, inpYear, boolForRent));
                }
                objNum++;
                inpYear = null;
                inpRent = null;
                boolForRent = false;
            }



            else if (choice == 3) {
                System.out.println("Please enter your car's color:");
                inpColor = myScanner.nextLine();
                do{
                    System.out.println("Please enter the year your car produced:");
                    try{
                        inpYear = myScanner.nextInt();
                    }
                    catch (Exception e) {
                        System.out.println("Please input a number.");
                    }
                    myScanner.nextLine();
                } while (inpYear == null);
                
                do{
                    System.out.println("Please enter whether your car for rent or not (Input Yes or No.):");
                    inpForRent = myScanner.nextLine();
                    if (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No"))) {
                        System.out.println("Please input yes or no.(Capitalization is ignored.)");
                    }
                }while (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No")));
                if (inpForRent.equalsIgnoreCase("Yes")) {
                    boolForRent = true;
                    
                    do{
                        System.out.println("Please enter your car's rent cost.(If it's unknown you can input 0.)");
                        try{
                            inpRent = myScanner.nextDouble();
                            if (inpRent < 0) {
                            System.out.println("Please input a positive number.");
                            }
                        }
                        catch (Exception e) {
                            System.out.println("Please input a number.");
                        }
                        myScanner.nextLine();
                    }while (inpRent == null || inpRent<0);
                }
                if (boolForRent == true && inpRent != 0) {
                    myCars.put(objNum, new ElectricCars(inpColor, inpYear, boolForRent, inpRent));
                }
                else {
                    myCars.put(objNum, new ElectricCars(inpColor, inpYear, boolForRent));
                }
                objNum++;
                inpYear = null;
                inpRent = null;
                boolForRent = false;
            }



            else if (choice == 4) {
                Integer inpNumRotors = null;
                Integer inpNumWings = null;
                System.out.println("Please enter your car's color:");
                inpColor = myScanner.nextLine();
                do{
                    System.out.println("Please enter the year your car produced:");
                    try{
                        inpYear = myScanner.nextInt();
                    }
                    catch (Exception e) {
                        System.out.println("Please input a number.");
                    }
                    myScanner.nextLine();
                } while (inpYear == null);
                
                do{
                    System.out.println("Please enter whether your car for rent or not (Input Yes or No.):");
                    inpForRent = myScanner.nextLine();
                    if (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No"))) {
                        System.out.println("Please input yes or no.(Capitalization is ignored.)");
                    }
                }while (!(inpForRent.equalsIgnoreCase("Yes") || inpForRent.equalsIgnoreCase("No")));
                if (inpForRent.equalsIgnoreCase("Yes")) {
                    boolForRent = true;
                    
                    do{
                        System.out.println("Please enter your car's rent cost.(If it's unknown you can input 0.)");
                        try{
                            inpRent = myScanner.nextDouble();
                            if (inpRent < 0) {
                            System.out.println("Please input a positive number.");
                            }
                        }
                        catch (Exception e) {
                            System.out.println("Please input a number.");
                        }
                        myScanner.nextLine();
                    }while (inpRent == null || inpRent<0);
                }

                do{
                    System.out.println("Please enter number of rotors your car has.");
                    try{
                        inpNumRotors = myScanner.nextInt();
                        if (inpNumRotors < 0) {
                        System.out.println("Please input a positive number.");
                        }
                    }
                    catch (Exception e) {
                        System.out.println("Please input an integer.");
                    }
                    myScanner.nextLine();
                } while(inpNumRotors == null || inpNumRotors < 0);

                do{
                    System.out.println("Please enter number of wings your car has.");
                    try{
                        inpNumWings = myScanner.nextInt();
                        if (inpNumWings < 0) {
                        System.out.println("Please input a positive number.");
                        }
                    }
                    catch (Exception e) {
                        System.out.println("Please input an integer.");
                    }
                    myScanner.nextLine();
                } while(inpNumWings == null || inpNumWings < 0);

                if (boolForRent == true && inpRent != 0) {
                    myCars.put(objNum, new FlyingCars(inpColor, inpYear, boolForRent, inpRent, inpNumRotors, inpNumWings));
                }
                else {
                    myCars.put(objNum, new FlyingCars(inpColor, inpYear, boolForRent, inpNumRotors, inpNumWings));
                }
                objNum++;
                inpYear = null;
                inpRent = null;
                boolForRent = false;
            }        
        } while (choice == 1 || choice == 2 || choice == 3 || choice == 4);

        myScanner.close();

        if (objNum == 0) {
            System.out.println("Understandable have a great day.");
        }
        else {
            for (int i = objNum-1;i>=0;i--) {
                Cars.getInfo(myCars.get(i));
            }
        }
        System.out.println(Cars.allMyCars);
    }
}