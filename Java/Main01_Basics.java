import java.util.Scanner;

public class Main1_Basics {
    public static void main(String[] args) {
        //My comment

        System.out.println("xd");
        long myNumber=123213213231213L;
        //float myFloat=3.14f;
        //boolean myCheck=true;
        //char myChar='@';
        String myText="My number is: ";
        System.out.println(myText+myNumber);
        
        Scanner myScanner=new Scanner(System.in);
        
        System.out.println("What is your name?: ");
        String inputName= myScanner.nextLine();

        System.out.println("What is your surname?: ");
        String inputSurname= myScanner.nextLine();
        
        System.out.println("How old are you?: ");
        int inputAge=myScanner.nextInt();

        myScanner.nextLine();
        System.out.println("What is your hometown?: ");
        String inputPlace=myScanner.nextLine();
        
        System.out.println("Hello "+inputName+" "+inputSurname+"!"+" You are "+inputAge+" years old. Your hometown is "+inputPlace+".");

        int numFriends= 10;

        System.out.println(numFriends/3);
        System.out.println(numFriends%3);

        numFriends++;

        System.out.println(numFriends);

        myScanner.close();

        /* 
         * Also my comment 
        */
    }
}