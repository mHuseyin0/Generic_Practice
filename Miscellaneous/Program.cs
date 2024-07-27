namespace Basics;

// Names does not have to be upper case
// If indices are not specified, they will start from 1 by incrementing 1
// If any index is specified, next ones will be incremented by 1
enum Days
{
    MON,
    TUE,
    WED,
    THU = 4,
    FRI,
    SAT,
    SUN
}

class Program{
    static void Main(string[] args){
        Console.Write("Vertical Tab\v");
        Console.WriteLine("Hello, World!\v");
        
        // int, double, bool, char, String, const
        // Inputs are always String
        int int1 = Convert.ToInt32("12");
        int1.GetType();

        // Taking input: Console.ReadLine();
        
        // Math class contains the relative methods

        Random random = new Random();
        int randNum = random.Next(1, 7); // Inclusive, exclusive

        String name = "xd";
        name = name.Insert(0, "xxd@");
        Console.WriteLine(name.Length);
        Console.WriteLine(name);
        
        /* If-Else statements, conditional operator, logical operators, switch-case statements,
         * for-while and do-while loops and arrays have the same syntax with java
         */

        String[] users = new String[5];

        for (int i = 1; i <= users.Length; i++)
        {
            users[i-1] = "User " + i;
        }
        
        // For each syntax is a little bit different
        foreach (String user in users)
        {
            Console.WriteLine(user);
        }
        
        // public keyword can be used at the beginning of the methods. Method syntax is also the same
        // Method overloading can be used in C#
        
        // params keyword can be used to take multiple variables of the same types
        // Notice that an array is not passed even though we use them as an array inside the function
        // Array must be 1-D in function definition
        Console.WriteLine(Multiply(2.5, 4.6, 8, 9.1));
        
        // try-catch-finally syntax is the same with java
        
        /* String interpolation (formatting in WriteLine) is similar to python
         * $ used instead of f, before the opening double quote.
         * variables are put in {}
         */
        
        // Multi Dimensional Arrays:
        int[,] matrix =
        {
            { 1, 2, 3 },
            { 4, 5, 6 },
            { 7, 8, 9 }
        };

        Console.WriteLine(matrix[1,1]);
        Console.WriteLine(matrix.Length); // Counts all dimensions
        Console.WriteLine(matrix.GetLength(1)); // Dimension number is needed
        
        /* Class syntax is also the same. Constructor is not neccessarily needed but can be used.
         * If constructor is not used, attributes can be assigned after creation of the object
         * Object creation has the same syntax with java, using new keyword.
         * Constructors can be overloaded
         *
         * Multiple inheritance is not supported. Multiple interfaces can be implemented though.
         * Inheritance syntax:
         * public class Car : Vehicle{
         *
         * Abstract class syntax:
         * abstract class Vehicle{
         *
         * In order to override a method, the method must be virtual, abstract, or already overridden
         *
         * Virtual and abstract method syntax:
         * public <virtual-abstract> void someFunction()
         * 
         * Virtual methods have an implementation and provide the derived classes with the option
         * of overriding it. Abstract methods do not provide an implementation and force the derived
         * classes to override the method. So, abstract methods have no actual code in them,
         * and (non-abstract) subclasses HAVE TO override the method.
         * Virtual methods can have code, which is usually a default implementation of something,
         * and any subclasses CAN override the method
         * 
         * Overridden method syntax:
         * public override void someFunction(){
         *
         * ToString() method is a significant one to override
         *
         * interface = defines a "contract" that all the classes inheriting from should follow
         * An interface declares "what a class should have"
         * An inheriting class defines "how it should do it"
         *
         * Methods in interfaces do not have a body
         * Interface syntax: (Notice the naming convention with leading I)
         * interface IVehicle{
         *
         * A class can inherit from at most one base class and many interfaces. Syntax:
         * Notice that base class (if there is) must come before the interfaces
         * class SubClass : BaseClass, Interface1, Interface2, (...){
         *
         * List class is the equivalent of the ArrayList in Java. Creation syntax are the same.
         * However, elements are accessed using indexing operator ([]) like regular arrays.
         * list.Add("Element") adds to the end
         * list.Remove("Element") removes the element
         * list.Insert(0, "Element") puts the element to the specified index
         * Sort, Reverse methods work in place. They change the actual List
         * IndexOf, LastIndexOf, Contains, Clear (Deletes all elements) are the other useful methods
         * ToArray method returns an array representation of the current List. It can be assigned to
         * an array. For example:
         * List<String> list = new List<String>();
         * String[] array = list.ToArray();
         *
         * GETTERS AND SETTERS are a little bit different:
         * 
         * class Car
         *  {
         *      private int speed; // public String Model {get; set;}
         *      Second implementation above is used when we can directly get and set properties
         *      without any restriction. If this is the case, public int Speed implementation below
         *      is not needed
         * 
         *      public Car(int speed)
         *      {
         *          Speed = speed;
         *      }
         *      public int Speed
         *      {
         *          get { return speed; }
         *          set                   
         *          {
         *              if (value > 500)
         *              {
         *                  speed = 500;
         *              }
         *              else
         *              {
         *                  speed = value;
         *              }
         *          }
         *      }
         *  }
         *
         * Generic types in C#: (Can be used in methods, classes, fields etc.)
         * public static void displayElements<Thing>(Thing[] array){
         */

        // To get integer values from enums, members should explicitly be casted

        foreach (Days day in Enum.GetValues(typeof(Days)))
        {
            Console.WriteLine($"{day} is the day {(int) day}.");
        }

        Console.WriteLine();
        Console.WriteLine($"{Days.MON} is the day {(int) Days.MON}.");
        Console.WriteLine($"{Days.TUE.ToString()} is the day {(int) Days.TUE}.");
        
        Thread mainThread = Thread.CurrentThread;
        Thread thread1 = new Thread(() => stopwatch(100));
        Thread thread2 = new Thread(switchLamp);

        thread1.Start();
        thread2.Start();
        //Console.ReadKey(); // To prevent terminal closing directly
    }

    static double Multiply(params double[] numbers)
    {
        double result = 1;
        foreach (double number in numbers)
        {
            result *= number;
        }

        return result;
    }
    
    public static void stopwatch(int start)
    {
        while (true)
        {
            start++;
            Thread.Sleep(1000);
            Console.WriteLine($"{start} seconds passed.");
        }
    }
    
    public static void switchLamp()
    {
        String status = "";
        while (true)
        {
            if (status == "ON")
            {
                status = "OFF";
            }
            else
            {
                status = "ON";
            }

            Console.WriteLine($"The lamp is {status}.");
            Thread.Sleep(5000);
        }
    }
}
