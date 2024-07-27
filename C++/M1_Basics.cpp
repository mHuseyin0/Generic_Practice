#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <iomanip>

namespace namespace1{
    int namespaceChar = 1;
}

namespace namespace2{
    int namespaceChar = 2;
}

typedef std::vector<std::pair<std::string, int>> pairList_t; //User defined types usually end with _t meaning type.
// Type aliases increase the readibility and reduce typos. Nevertheless, "using" keyword is more common and works better with templates.
using string_t = std::string;

class Human{
    private:
        int IDNum = 0;
    public:
        std::string name;
        int age;
        bool alive = true;

        void walk(){
            std::cout << this->name << " is walking.";
        }

        int getIDNum(){
            if (this->IDNum == 0){
                std::cout << "\n" << this->name << " does not have a ID number.\n";
                return 0;
            }
            else{
                return this->IDNum;
            }
        }
        
        // Setters can be used inside the constructors as well.
        void setIDNum(int newIDNum){
            if (newIDNum <= 0){
                std::cout << "ID number must be greater than 0. Please try again.";
            }
            else{
                this->IDNum = newIDNum;
            }
        }
};

class Car{
    public:
        std::string name;
        bool useElectricity;
        int year;
        double price;

        Car(std::string name, bool useElectricity){
            this-> name = name;
            this-> useElectricity = useElectricity;
        }
        Car(int year, double price){
            this-> year = year;
            this-> price = price;
        }
        /*
        Car(std::string x, bool y){
            name = x;
            useElectricity = y;
        }
        This will also work.
        */
};

class Animal{
    public:
        std::string name;
        bool alive = true;

        Animal(std::string name){
            this-> name = name;
        }
        
        void eat(){
            std::cout << "\n" << this->name << " is eating.";
        }
};

class Bird : public Animal{
    public:
    bool canFly;

        Bird(std::string name, bool canFly) : Animal(name), canFly(canFly){}
        
        void fly(){
            canFly ? std::cout << "\n" << this->name << " is flying." : std::cout << "\n" << this->name << " cannot fly.";
        }
};

int main(int argc, char const *argv[]){
    /*
    Try to not pass any argument to main function.
    */
    std::cout << "Hello, "; // standard:: character output
    std::cout << "This is C++." << std::endl;// Flushes the output buffer unlike newline char.
    std::cout << "Have a nice day!" << '\n';// Better than endl performance wise.
    std::cout << "This is another newline.\n";

    int x;
    x = 10;
    int y = 5;
    double z = 5.55;
    char singleCharacter = '#';
    bool isSth = true;
    bool isSthElse = false;

    const double PI = 3.14159265; // 265 will not be holded.

    std::string tip = "Strings are provided by std namespace.";

    // Double colon is the scope resolution operator.

    std::cout << singleCharacter << x+y << "\n" << z << "\n";
    std::cout << isSth << " or " << isSthElse <<"\n";
    std::cout << PI;

    int namespaceChar = 0;

    std::cout << "\nNamespace 1: " << namespace1::namespaceChar;
    std::cout << "\nNamespace 2: " << namespace2::namespaceChar;
    std::cout << "\n" << namespaceChar;

    using namespace namespace1;
    /* If declaration in the main method was deleted, namespaceChar would be got from namespace1. However, if the variable already exists
    in current namespace, it will be used like this case.*/
    std::cout << namespaceChar;

    using std::cout;
    using std::string;

    cout << "\nThis is easier!\n";

    int toConvert = 100;
    cout << (char) toConvert;

    /*
    "<<": Insertion operator
    ">>": Extraction operator
    */
    /*string_t name;
    cout << "\nPlease input your name: ";
    std::cin >> name;
    cout << "\nHello, " << name << "!\n";

    string_t includeSpace;
    cout << "Please input something including space: ";
    std::getline(std::cin >> std::ws, includeSpace); // std::cin will not return characters after a space, but getline works properly with space including texts.
    cout << "\n" << includeSpace << "\n"; // If we want to use getline after a std::cin, we should use std::ws to clean whitespaces.(std::cin gives \n to the buffer after input.)
    // Nevertheless, when something including space entered to std::cin, getline accepts all the words except the first one and does not take new input.
    */
    cout << "\n" << std::max(2, 4) << "\n";
    cout << std::min(2, 4) << "\n";
    // Functions below are from cmath.
    cout << pow(2, 4) << "\n"; // There is no exponent operator like **.
    cout << pow(256, (double) 1/2) << "\n";
    cout << pow(10, -1) << "\n";
    cout << sqrt(4) << "\n";
    cout << abs(-5) << "\n";
    cout << round(3.5) << "\n";
    cout << ceil(4.1) << "\n";
    cout << floor(6.9) << "\n";

    // if, else if and else syntax is the same with java.
    /*int monthNum;
    cout << "Please input a month number between 1 and 12: ";
    std::cin >> monthNum; 
    cout << "\n";

    switch (monthNum){
        case 1:
            cout << "It's January.";
            break;
        case 2:
            cout << "It's February.";
            break;
        case 3:
            cout << "It's March.";
            break;
        case 12:
            cout << "It's December.";
            break;
        default: cout << "This is not between 1-12!";
    }*/

    // Ternary operator: ?
    // condition ? ifTrueDoThis : ifFalseDoThat;
    // switch and ternary operator syntax is also the same with java.
    // Logical operators: &&: and, ||: or, !: not
    // Bitwise operators: &: and, |: or, ^: xor, ~: not, <<: leftshift, >>: rightshift

    string_t testString = "This is a test string.";
    string_t emptyString = "";
    cout << testString.length() << "\n";
    cout << emptyString.empty() << "\n"; // Returns 1 if empty and 0 else.
    testString.clear();
    testString.append("This is new string.");
    testString.insert(0, "This is appended string.");
    cout << testString << "\n";
    cout << testString.at(0) << "\n";
    cout << testString.find(" ") << "\n";
    testString.erase(0, 5); // inclusive, exclusive
    cout << testString << "\n";

    // When you declare a bool or an int but not assigned them, their default value is 0.
    // Java does not have this property.

    // While, do-while, for, for-each loop syntaxes and break, continue keywords are the same with java.
    // Auto keyword while declaring variables will assign automatically a type to that variable. (Sometimes it can be risky.)

    srand(time(NULL)); // Set seed for rand() function. NULL exactly means 0.
    int randNum = rand();
    cout << randNum << "\n"; // If you want to create random numbers between 0 and 10 for example, (randNum % 10) + 1 will work.(Only with small numbers like 10 or maybe a few hundreds.)

    /* 
    Function defining syntax is also same with java. However, if you will define the body of a function after the main function,
    (due to aesthetic issues) it must be declared before the main function.
    Example declaration: 
    void doSomething();
    
    Example definition (after the main function):
    void doSomething(){
        body;
    }
    
    Also overloaded functions can be used.(Functions with the same name but accept different types or different number of arguments.)
    Global variables are defined outside of any function.
    If there is two variables with the same name in both global and local scope, local one will be used by default.
    Nevertheless, if we want to use global varaible we can use scope resolution operator(::) before the variable.
    ::myVariable will search the variable in the global scope for example.
    
    std::cin.clear();
    fflush(stdin);
    These two lines of code will clear the input buffer.

    */

   std::string colors[] = {"Blue","Black","White"};

   colors[3] = "Yellow";
   colors[5] = "Green";

   cout << colors[4] << "\n"; // Passing just the array will return the memory location.

    int emptyArray[2]; // Number of items must be passed if we do not initialize the array. Nevertheles, it will accept more than that value.
    emptyArray[0] = 0;
    emptyArray[1] = 1;
    emptyArray[2] = 2;

    cout << emptyArray[2] << "\n";

    std::string randString = "A random string.sdaaaaa";
    cout << sizeof(randString) << " bytes.(String)\n";
    // If you pass a variable which contains string, it will be always 32 bytes.
    // However, if you pass the string directly, it will change regarding of the length of the string.
    // (Passing single characters in single quotes as a char is more efficient than passing in double quotes as a string.)
    cout << sizeof(1132132) << " bytes.(int)\n"; // Always 4 bytes.
    cout << sizeof(1.0) << " bytes.(double)\n"; // Always 8 bytes.
    cout << sizeof('@') << " bytes.(char)\n"; // Always 1 byte.
    cout << sizeof(true) << " bytes.(bool)\n"; // Always 1 byte.
    cout << sizeof(emptyArray) << " bytes.(array)\n";
    cout << sizeof(colors) << " bytes.(array)\n";
    // Size of an array is changable according to number of elements it consists of. (Equals to the sum of elements' bytes.)
    // Dividing the sizeof an array by an element of that array will give the number of elements. (Because an array can only contain 1 data type.)
    // This can be used to iterate over an array using a for loop.

    /*
    How to pass an array to a function: (Array size cannot be found in the function, passing another argument for that is one of the solutions.)
    
    Array initialization:
    double myArray[] = {1.2, 1.3, 1.5};
    
    Function definition:
    void doSomething(double anArray[]){

    }

    Function call:
    doSomething(myArray)

    Arrays do not have a specific search and sort methods, they should be written manually (using algorithms).*/

    std::string arrayToFill[100];

    fill(arrayToFill, arrayToFill + 25, "First 25");
    fill(arrayToFill + 75, arrayToFill + 100, "Last 25");

    for (int i = 1; i <= 100; i++){
        cout << "Element " << std::setfill('0') << std::setw(3) << i << ": " << arrayToFill[i-1] << "\n"; // Adding leading zeros.
    }
 
    cout << "\n";
    std::string MDarray [4][20];


    for (int i = 0; i < sizeof(MDarray)/sizeof(MDarray[0]); i++){
        for (int j = 0; j < sizeof(MDarray[i])/sizeof(MDarray[i][0]); j++){
            MDarray[i][j] = '#';
            cout << MDarray[i][j]; 
        }
        cout << "\n";
    }

    /*
    & is address-of operator which can be used before variable names to get memory address
    If your variables in a function definition are accepted with memory addresses, they will change the original value, unlike a normal function.
    This is called pass-by-reference. Normal way is called pass-by-value. Here is an example:
    
    void doSomething(int &x, std::string &y){

    }
    You need to use address-of operator neither in the body nor when calling.
    */
    std::string memoryTest = "Test";
    int memoryTest2 = 5;
    cout << &memoryTest << "\n";
    cout << &memoryTest2 << "\n";

    /* "*" is also dereference operator when we used it before variables*/

    std::string pointerTest = "This is how pointers work";
    std::string *pPointerTest = &pointerTest; // Leading p is the naming convention of pointers in c++

    cout << *pPointerTest;
    
    // nullptr keyword is used to create a null pointer so that we can check if the pointer was assigned to a value or it is null

    cout << "\n";
    int *nullPointer = nullptr;
    cout << nullPointer << " :Null Pointer";

    int aNumber = 5;
    int *aPointer = nullptr;
    aPointer = &aNumber;
    if (aPointer != nullptr){
        cout << "\n" << "This pointer is not null and its value is: " << *aPointer << "\n";
    }

    // new and delete keywords are used to allocate and deallocate memory dynamically (after compilation, while running)
    // new keyword allocates memory in the heap rather than the stack. It's useful when we do not know how much memory we will need.
    // This makes our program more flexible, especially when accepting user input.

    // This part behaves strange. No idea.
    /*std::string *pointer = NULL;
    int userInputSize = 5;
    pointer = new std::string[userInputSize];
    pointer[0] = "First element";
    pointer[1] = "Second element";
    // Take inputs to put in the array from user (maybe with a for loop)
    delete[] pointer;
    cout << pointer[1] << std::endl << pointer[0] << std::endl;
    cout << "Pointer: "; 
    cout << pointer << "\n";
    cout << "Value: "; 
    cout << *pointer << "\n";*/

    /*
    Function Templates:

    template <typename T, typename U>
    auto doSomething(T x, U y){
        body
    }

    This function will accept and return any data type. This is what function templates.
    In case inputs are different data type, we created two different type. It's also possible to make both types T.
    Also, thanks to auto keyword output type will be what it should be.
    Using T is just a convention here.

    Function templates can be used instead of overloading functions.
    */

    /*
    Structs:
    Class-like things without methods

    Outside the main function define a struct with struct keyword:
    struct strcuct1{
        std::string name;
        int arg1;
    };

    In the main function:
    struct1 member1;
    member1.name = "First member";
    member1.arg1 = 1;

    If you want to pass a member to a function and change its properties, make sure that you are passing by reference:

    void doSomething(struct1 &member){
        body
    }

    */

    /*
    Enums:
    A user-defined data type that consists of paired named-integer constants. GREAT if you have a set of potential options
    
    Outside the main function:

    enum Days {Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6};
    If you do not assign integer values, it will be assigned automatically from zero like above example.
    It's free to assign any integer as long as there is no duplicate members.

    In the main function:

    Days today = Monday;

    Switch statements do not accept values other than int, char and enum like strings.
    Therfore enums can be useful to check string-like things
    */

    Human human1;
    human1.name = "Human1";
    human1.age = 34;
    human1.walk();

    Car car1("Car1", false);
    cout << car1.name;
    Car car2(2015,5000);
    cout << car2.price;
    human1.setIDNum(5);
    cout << human1.getIDNum();

    Bird bird1("Bird1",true);
    cout << "\n" << bird1.canFly;
    bird1.eat();
    bird1.fly();
}// Tip: C++ does not care about indentation like Java and JavaScript.(Only python does among these four.)
