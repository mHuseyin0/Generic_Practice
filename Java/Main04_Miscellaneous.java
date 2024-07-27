import java.util.*;

public class Main4_Miscellaneous {
    public static void main(String[] args) {
        
        boolean x = false;
        boolean y = false;


        if (x) {
            System.out.println("Hello!");
        }
        else if(y) {
            System.out.println("Hey!");
        }
        else {
            System.out.println("Hi!");
        }

        String day = "Wednesday";

        switch(day) {
            case "Monday": System.out.println("It's Monday.");
            break;
            case "Tuesday": System.out.println("It's Tuesday.");
            break;
            case "Wednesday": System.out.println("It's Wednesday.");
            break;
            case "Thursday": System.out.println("It's Thursday.");
            break;
            case "Friday": System.out.println("It's Friday.");
            break;
            case "Saturday": System.out.println("It's Saturday.");
            break;
            case "Sunday": System.out.println("It's Sunday.");
            break;
            default: System.out.println("Please enter a day beginning with a upper case and continuing with lower cases.");
        }

        double a = 0;

        if (!(a%2==0 || a%3==0)) {
            System.out.println("Your number is not a multiple of 2 or 3.");
        }
        else if (a==0) {
            System.out.println("Your number is 0.");
        }
        else if (a%2==0 && a%3==0) {
            System.out.println("Your number is a multiple of 6.");
        }
        else if (a%2==0) {
            System.out.println("Your number is a multiple of 2.");
        }
        else {
            System.out.println("Your number is a multiple of 3.");
        }

        String b = ":)";

        if (!b.equalsIgnoreCase("xd") ) {
            System.out.println("Have a nice day!");
        }

        Scanner myScanner = new Scanner(System.in);

        //String userInput = "xd";

        //String password ="xd";
        
        //Do command will be executed for 1 time, then while condition will be checked.
        //do {
        //    System.out.println("Please input the password.");
        //    userInput = myScanner.nextLine();
        //} while (!userInput.equalsIgnoreCase(password)); 

        myScanner.close();

        for(int i =1; i<=10; i+=1) {
            System.out.println("Loop execution counter: "+i);
        }

        //int[] figures = {0,1,2,3,4,5,6,7,8,9};
        
        //for (int i = 0;i<=9;i++) {
        //    System.out.println(figures[i]);
        //}

        String[] letters = new String[29];

        letters[0]= "A";
        letters[1]= "B";
        letters[2]= "C";

        for (int i=1;i<=29;i++) {
            System.out.println("Letter"+i+": "+letters[i-1]);
        }

        String[][] trigonometric_Funcs = new String[2][4];

        trigonometric_Funcs[0][0]="1";
        trigonometric_Funcs[0][1]="0";
        trigonometric_Funcs[0][2]="-1";
        trigonometric_Funcs[0][3]="0";
        trigonometric_Funcs[1][0]="0";
        trigonometric_Funcs[1][1]="1";
        trigonometric_Funcs[1][2]="0";
        trigonometric_Funcs[1][3]="-1";

        System.out.println(trigonometric_Funcs.length);
        System.out.println(trigonometric_Funcs[0].length);
        System.out.println(trigonometric_Funcs[1].length);

        int[][] myArray = {{1,0,-1,0},
                            {0,1,0,-1}};

        System.out.println(myArray.length);
        System.out.println(myArray[0].length);
        System.out.println(myArray[1].length);

        String xdString = "  AaBbCcDdxxxa  ";
        String blankString = "   ";
        //double myDouble = 3.14159265;
        boolean boolxd = xdString.equals("xd");
        System.out.println(boolxd);
        System.out.println(xdString.length());
        System.out.println(xdString.charAt(2));
        System.out.println(xdString.indexOf("k"));
        System.out.println(blankString.isEmpty());
        System.out.println(blankString.isBlank());
        System.out.println(xdString.toUpperCase());
        System.out.println(xdString.trim());
        System.out.println(xdString.replace("x","j"));

        //Referance data types contain useful methods, but they are slow to work with when compared with primitives. 
        //Autoboxing means primitive --> Wrapper Class (Unboxing is the reverse of this.)

        //ArrayLists just can contain reference data types.
        ArrayList<String> myList = new ArrayList<>();
        myList.add("element1");
        myList.add("element2");
        myList.add("element1");
        myList.set(2, "element3");
        System.out.println(myList.size());
        for (int i=0;i<myList.size();i++) {
            System.out.println(myList.get(i));
        }
        
        ArrayList<String> myList1 = new ArrayList<>(); 
        myList1.add("L1E1");
        myList1.add("L1E2");
        ArrayList<String> myList2 = new ArrayList<>();
        myList2.add("L2E1");
        myList2.add("L2E2");
        myList2.add("L2E3");
        myList2.add("L2E4");
        ArrayList<String> myList3 = new ArrayList<>(); 
        myList3.add("L3E1");
        myList3.add("L3E2");
        myList3.add("L3E3");
        
        ArrayList<ArrayList<String>> myList4 = new ArrayList<>();
        myList4.add(myList1);
        myList4.add(myList2);
        myList4.add(myList3);
        System.out.println(myList4.get(1).get(2));

        for (ArrayList<String> i : myList4) {
            System.out.println(i);
        }

        int sumFigures = add(23,56,1);

        System.out.println(sumFigures);

        ArrayList<Integer> figures = new ArrayList<>();
        figures.add(1);
        figures.add(2);
        figures.add(3);
        figures.add(4);
        figures.add(5);
        figures.add(6);
        figures.add(7);
        figures.add(8);
        figures.add(9);

        System.out.println(addition((figures)).get(0));
        System.out.println(addition((figures)));

        String theString = "xd";
        Integer theInteger = 10000000;
        boolean theBool = true;
        double theDouble = 20;
        char theChar = '@';

        System.out.printf("My string is: %s",theString);
        System.out.printf(" My integer is: %d",theInteger);
        System.out.printf(" My boolean is: %b",theBool);
        System.out.printf(" My double is: %f",theDouble);
        System.out.printf(" My character is: %c",theChar);
    
        System.out.printf("The string is:%-5s",theString);
        System.out.printf("The string is:%5s",theString);
        System.out.println("");
        System.out.println(Math.PI);
        System.out.printf("Pi number is:%.4f",Math.PI);
        System.out.println("");
        System.out.printf("Your number is:%20d",theInteger);
        System.out.println("");
        System.out.printf("Number:%015f",theDouble);
        System.out.println("");
        System.out.printf("%,d",theInteger);
        System.out.println("");
        System.out.println("");

        final double THEPI = 3.14159265;
        System.out.println(THEPI);

        

    }

    static int add(int x,int y) {
        return x+y;
    }

    static int add(int a, int b,int c) {
        return a+b+c;
    }

    static ArrayList<Integer> addition(ArrayList<Integer> numbers) {
        int sum=0;
        for (Integer i : numbers) {
            sum+=i;
        }
        ArrayList<Integer> product = new ArrayList<>();
        product.add(sum);
        return product;
    }
}