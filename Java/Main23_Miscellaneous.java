
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.util.HashMap;
import java.util.Scanner;

import javax.swing.JButton;
import javax.swing.JFrame;

//Enums cannot be changed after compilation.
enum Days{
    MONDAY(1),TUESDAY(2),WEDNESDAY(3),THURSDAY(4),FRIDAY(5),SATURDAY(6),SUNDAY(7);

    int number;

    Days(int number) {
        this.number = number;
    }
}

class AgeException extends Exception {
    AgeException(String message) {
        super(message);
    }
}

class Outside {
    int x = 5;
    class Inside {
        int y = 10;

        static void sum(int a, int b) {
            System.out.println(a+b);
        }
    }

    void greeting() {
        System.out.println("Hello!");
    }
}

@FunctionalInterface
interface MyInterface {
    public void message();
}
@FunctionalInterface
interface MyInterface2 {
    public void operations(int a, int b);
}

class myGenericClass <T extends Number, T2>{
    T x;
    T2 y;
    myGenericClass(T x, T2 y) {
        this.x = x;
        this.y = y;
    }
    public HashMap<T,T2> getValues() {
        HashMap<T,T2> myMap = new HashMap<>();
        myMap.put(x, y);
        return myMap;
    }
    
}


public class Main23_Miscellaneous {
    public static void main(String[] args) {
        System.out.println("       mha".concat(" xd         ").toUpperCase().trim());

        Days myDay = Days.MONDAY;

        isWeekend(myDay);

        Scanner myScanner = new Scanner(System.in);
        
        System.out.print("Please enter your age: ");
        int age = myScanner.nextInt();
        try{
            checkAge(age);
        } catch (Exception e) {
            System.out.println("A problem occured: " + e);
        }
        myScanner.close();

        Outside.Inside.sum(new Outside().x, new Outside().new Inside().y);

        new Outside() {
            @Override
            void greeting() {
                System.out.println("Hey!");
            }
        }.greeting();

        MyInterface myInterface = () -> System.out.println("Hello!");
        myInterface.message();
        
        MyInterface2 myInterface2 = (a,b) -> System.out.println(a+ b);
        myInterface2.operations(7, 6);
        
        MyInterface2 myInterface3 = (a,b) -> {
            System.out.println("Addition: " + (a+b));
            System.out.println("Multiplication: "+ (a*b));
        };
        myInterface3.operations(9, 9);

        JButton myButton = new JButton();
        myButton.addActionListener((e) -> System.out.println("This button has been pressed."));
        myButton.setPreferredSize(new Dimension(100,50));

        JFrame myFrame = new JFrame();
        myFrame.getContentPane().setBackground(Color.black);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setLayout(new FlowLayout(FlowLayout.CENTER));
        myFrame.setLocationRelativeTo(null);
        myFrame.add(myButton);
        myFrame.pack();
        //myFrame.setVisible(true);

        Integer[] myList = {1,2,3,4,5};

        printArray(myList);

        System.out.println(getFirst(myList));

        myGenericClass<Double,String> myData = new myGenericClass<>(2.43, "xd");
        myGenericClass<Integer,Character> myData2 = new myGenericClass<>(0,'@');
        System.out.println(myData.getValues());
        System.out.println(myData2.getValues());

    }

    static <T> T getFirst(T[] myArray) {
        return myArray[0];
    }

    static <T> void printArray(T[] myArray) {
        System.out.println(myArray[0].getClass().getSimpleName() + " is your data type.");
        System.out.println("Array index:");
        for (T x : myArray) {
            if (x == myArray[myArray.length-1]) {
                System.out.print(x+".");
                System.out.println();
            }
            else {
                System.out.print(x+ ", ");
            }
        }
    }

    static void checkAge(int age)throws AgeException {
        if(age < 18) {
            throw new AgeException("\nThose who younger than 18 are not accepted.");
        }
        else {
            System.out.println("You signed up.");
        }
    }

    static void isWeekend(Days day) {
        if (day == Days.SATURDAY || day == Days.SUNDAY) {
            System.out.println("This is weekend.");
            System.out.printf("This is day %d in a week.", day.number);
            System.out.println("");
        }
        else {
            System.out.println("This is a weekday.");
            System.out.printf("This is day %d in a week.", day.number);
            System.out.println("");
        }
    }
}
