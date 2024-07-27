#include <stdio.h>
#include <stdbool.h> // To work with booleans
#include <string.h> // Includes string methods
#include <stdlib.h> // To get random number
#include <time.h> // To get random number
#include <math.h>

void printDash(){
    printf("\n-----------------------------------------\n");
}

void printAgeName(int age, char name[]){
    printf("\nYour age: %d\nYour name: %s\n", age, name);
}

void functionPrototype(int, char []); // Variable names may not been included before the main function of a prototype

// String with 50 length has "name" nickname from now on
typedef char name[50];

// Since struct created with a typedef, struct keyword is not needed while creating a member
typedef struct
{
    name username;
    name password;
    int id;
} User;

// Enums normally start from 0 to enumerate
enum Day{Sun = 1, Mon = 2, Tue = 3, Wed = 4, Thu = 5, Fri = 6, Sat = 7};


int main() {
    printf("Hello, World!\n");// Comment
    char string[] = "This is a string in C language.";
    printf(string);

    float e = 2.718281; // 4 bytes
    const double PI = 3.141592653589793; // 8 bytes
    printf("\ne number:\t%0.6f", e);
    printf("\npi number:\t%0.15lf", PI);

    bool isCorrect = true; // 1 byte

    char symbol = '?'; // 1 byte
    char char1 = 42; // char can store -128 to 127 %d
    // %d will display 127 and %c will display ASCII value
    printf("\nASCII %d is %c.", char1, char1);

    unsigned char char2 = 255; // can store 0 to 255

    short int int1 = 213; // 2 bytes, can store between -32.768, 32.767
    unsigned short int int2 = 0; // can store between 0, 65.535
    // short int can be declared as short directly

    int int3 = 7899; // 4 bytes can store more than between ± 2 billion
    unsigned int int4 = 13231; // can store more than between 0 to 4 billion, displayed with %u
    // int is declared as long int explicitly, so long is declared with double long keyword

    long long int int5 = -21321213; // 8 bytes, between ±9 quintillion, %lld
    unsigned long long int int6 = 32121323U; // between 0 and +18 quintillion %%llu

    printf("\n%llu", int6);

    int input1;
    /*printf("\nPlease input an integer: ");
    scanf("%d", &input1);// address of operator:&

    char input2[16]; // 16 bytes
    printf("\nPlease input a string: ");
    //scanf("%s", &input2); // Cannot take inputs including whitespaces
    fgets(input2, 16, stdin); // Can take inputs including whitespace, do not use & here
    // However, adds a newline character at the end of the input string
    input2[strlen(input2)-1] = '\0'; // This prevents newline char at the end
    printf("\n%s", input2);
    */
    // sqrt, pow, round, ceil, floor, fabs (absolute value), log, sin, cos, tan functions come with math.h

    // Syntax of conditional statements and logical operators are the same with java

    printDash();
    // Argument passing is also the same with java

    printAgeName(12, "xd");
    functionPrototype(5, "xdd");

    char string1[16] = "Test";
    char string2[16] = "String";

    strcat(string1, string2); // Add string2 to the end of string1
    printf("\n\n%s\n%s", string1, string2);

    strncat(string1, string2, 3); // Add the first 3 char of string2
    printf("\n\n%s\n%s", string1, string2);

    strncpy(string1, string2, 1); // string1[0,1] = string2[0,1]
    printf("\n\n%s\n%s\n", string1, string2);

    strcpy(string1, string2); // string1 = string2
    printf("\n\n%s\n%s", string1, string2);

    int result1 = strcmp(string1, string2); // If strings are the same the result is 0
    int result2 = strncmp(string1, string2, 3);

    printf("\nResult1: %d\nResult2: %d\n", result1, result2);
    printf("\n%d\n", strlen(string1));

    // Loop syntax is completely the same with java

    // Array syntax is almost the same with java except the location of square brackets
    // java: int[] ages;
    // C: int ages[];

    double array1[] = {2.5,5.6,6.7,7.8};
    int sizeInBytes = sizeof(array1);
    printf("Size of the array: %d\n", sizeInBytes / sizeof(double));
    // Instead of sizeof(double), sizeof(array1[0]) may be used.

    char stringArray[][20] = {"Python", "C++", "JavaScript"};
    // 20 is max length of a string here. This is a 2D array
    // strcpy() should be used to change some value
    printf("%s\n", stringArray[0]);

    // Structs are like classes without methods
    struct Human
    {
        name name; // Typedef used
        int age;
    };

    struct Human human1;
    struct Human human2;

    strcpy(human1.name, "Human1");
    human1.age = 25;

    strcpy(human2.name, "Human2");

    User user1 = {"User1", "password1", 1};
    printf("%s:\n\tPassword: %s\n\tID: %d\n", user1.username, user1.password, user1.id);

    struct Human people[] = {human1, human2};

    for(int i = 0; i < sizeof(people) / sizeof(struct Human); i++)
    {
        printf("Name: %s\n", people[i].name);
    }

    // Enums make the code more readable. They are not String, but they can be treated as int
    enum Day today = Sat;
    printf("Today's number: %d\n", today);

    srand(time((0))); // This is the seed for random numbers
    // If that is excluded, our number will be the same in each run

    int randNum = rand() % 101; // rand() function will return a random int between 0 and 32k
    // So we may use modulus operator to get a random between 0 and n-1

    printf("Random Number: %d\n", randNum);

    /* Bitwise operators: those can be applied to ints so that result will be an int
     * &: AND
     * |: OR
     * ^: XOR
     * <<: Left Shift
     * >>: Right Shift
     * Shifting operators can be used with ints to shift the binary representation by n
     */

    int binary = 100;
    int binaryNot = ~binary;
    int *pBinary = &binary; // * is indirection operator (pointer). Notice the naming convention of the pointers
    int *pBinaryNot = NULL; // It's a good practice to assign null if we are not initializing a pointer
    pBinaryNot = &binaryNot;

    printf("Binary NOT of %d: %d\n", binary, binaryNot);

    // Notice that there are 4 bytes between addresses of 2 ints
    printf("Address of %d: %p\n", binary, &binary);
    printf("Address of %d: %p\n", binaryNot, &binaryNot);

    printf("Address of %d: %p\n", binary, pBinary);
    printf("Value of %p: %d\n", pBinary, *pBinary); // To get the value of a pointer, * is used

    printf("Size of %d: %lu Bytes\n", binary, sizeof(binary));
    printf("Size of %p: %lu Bytes\n", pBinary, sizeof(pBinary)); // Hexadecimal value should be stored in 8 bytes

    // Pointers can be passed to functions

    FILE *pFile = fopen("test.txt", "r");

    //fprintf(pFile, R"(\nThis is also appended by C.)");

    const int BUFFER_SİZE = 255;
    char buffer[BUFFER_SİZE];
    printf("This is read by C:\n");
    while(fgets(buffer, BUFFER_SİZE, pFile) != NULL) // Function returns NULL when there is nothing to read
    {
        printf("%s", buffer);
    }

    fclose(pFile); // Do not dereference it

    //remove("test.txt"); // If deletion of the file is successful, the function will return 0

    return 0;
}

void functionPrototype(int age, char name[]){
    printf("\nYour age: %d\nYour name: %s\n", age, name);
}
