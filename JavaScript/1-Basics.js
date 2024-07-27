console.log("This is text.");
console.log('This is another text.')
//window.alert("This is an alert!!!")
//This is comment.
/*Another
comment*/
//In JavaScript semicolons doesn't have to be used.
//To declare a variable, var, let or const must be used.

let myNumber1 = 21;    //number
let myString1 = "Hi";  //string
let myBoolean1 = false; //boolean
//Arithmetic operators are the same with python

console.log(myNumber1+myString1);
console.log(myNumber1, "User!");

document.getElementById("0").innerHTML = "This text was set by JS.";

document.getElementById("button1").onclick = function(){
    let myInput1 = document.getElementById("input1").value;
    console.log(myInput1) /*If this line were outside the function, it wouldn print 'undefined' properly.*/
    document.getElementById("label1").innerHTML = "Your input: " + myInput1;
}
//let myInput2 = window.prompt("Please enter a value: ");
//Inputs are always string

let myValue1 = "10";
myValue1 = Number(myValue1);
console.log(typeof myValue1);
console.log(Boolean(""));
console.log(String(2.718));
console.log(Number("xd"));
console.log(Number(true));

const PI = 3.14159265;

console.log(Math.round(PI)); //floor(x), ceil(x), pow(x, y), sqrt(x), abs(x), are also useful Math functions
console.log(Math.min(Math.E, Math.PI, Math.SQRT1_2, Math.random()*2));

let myString2 = "    Hi! This is a test string .    ";

console.log(myString2.split(" ",3));
console.log(myString2.trim());
console.log(myString2);
console.log(myString2.trimStart().toUpperCase()); //Method chaining
myString2 = myString2.trimEnd()
console.log(myString2);
console.log(myString2.length);
console.log(myString2.charAt(2));
console.log(myString2.search("t"));
console.log(myString2.indexOf("t"));
console.log(myString2.lastIndexOf("t"));
console.log(myString2.slice(5));
console.log(myString2.slice(-4));
console.log(myString2.slice(5,10));
console.log(myString2.endsWith("."));
console.log(myString2.replaceAll("t","T"));
console.log(myString2.replace("t","T"));

myString2 = myString2.trim();
let myString2SecondSpace = myString2.indexOf(" ",myString2.indexOf(" ")+1);
console.log(myString2SecondSpace);
console.log("Your third word is: " + myString2.slice(myString2SecondSpace,myString2.indexOf(" ",myString2SecondSpace+1)));

let x = 0;

if (x == 0){
    console.log("Your number is 0.");
}
else if(x > 0){
    console.log("Your number is positive.");
}
else{
    console.log("Your number is negatiive.");
}

document.getElementById("button2").onclick = function(){
    if (document.getElementById("checkbox1").checked){
        console.log("Checkbox is currently checked.");
    }
    else{
        console.log("Checkbox is not checked at the moment.");
    }

    if (checkbox1.checked) {
        console.log("You selected number 1.");
    }
    else if (checkbox2.checked) {
        console.log("You selected number 2.");
    }
    else if (checkbox3.checked) {
        console.log("You selected number 3.");
    }
    else{
        console.log("You haven't selected anyone.");
    }
}

const checkbox1 = document.getElementById("radio1");
const checkbox2 = document.getElementById("radio2");
const checkbox3 = document.getElementById("radio3");

let myVariable1 = "A";
let myVariable2 = 50;

switch(myVariable1.toUpperCase()){
    case "A" :
        console.log("Your grade is A.");
        break;
    case "B" :
        console.log("Your grade is B.");
        break;
    case "D" :
        console.log("Your grade is D.");
        break;
    case "F" :
        console.log("Your grade is F.");
        break;
    default:
        console.log("Invalid input!");
}
switch(true){
    case myVariable2 > 100:
        console.log("You probably would get A+, if it were in the scale.");
        break;
    case myVariable2 >= 80:
        console.log("Your letter grade is A.");
        break;
    case myVariable2 >= 75:
        console.log("Your letter grade is A-.");
        break;
    case myVariable2 >= 70:
        console.log("Your letter grade is B+.");
        break;
    case myVariable2 >= 65:
        console.log("Your letter grade is B.");
        break;
    case myVariable2 >= 60:
        console.log("Your letter grade is B-.");
        break;
    case myVariable2 >= 55:
        console.log("Your letter grade is C+.");
        break;
    case myVariable2 >= 50:
        console.log("Your letter grade is C.");
        break;
    case myVariable2 >= 45:
        console.log("Your letter grade is C-.");
        break;
    case myVariable2 >= 40:
        console.log("Your letter grade is D+.");
        break;
    case myVariable2 >= 30:
        console.log("Your letter grade is D.");
        break;
    case myVariable2 < 0:
        console.log("How have you succeded getting a negative grade?");
        break;
    case myVariable2 < 30:
        console.log("Your letter grade is F.");
        break;
    default:
        console.log("INVALID INPUT!");
}

let myVariable3 = "10";
if (myVariable3 == 10) {
    console.log("Your input is probably 10.");
}
if (myVariable3 === 10) { // Strict equality operator (checks the data type unlike comparison operator(==))
    console.log("Your input is definitely 10.");
}
else{
    console.log("Your input is not 10.");
}
// != operator is also checks stricly like ===
// && means AND, || means OR, ^ means XOR
//(do-)while and for loop syntaxes are the same with Java
//break and continue keywords are also exist
x = 1
while (x<10){
    if (x==4){
        x++;
        continue;
    }
    if (x==7){
        break;
    }
    console.log(x);
    x++;
}

//.innerHTML() function can be used with += operator to append something (Even tags like "<br>" will work)

//functions have access to global variables
//if you don't pass any value to y, it will be "undefined"

function function1(y){
    console.log(x,y);
}
function function2(){
    let y = 5;
    function1();
}
function2();

function function3(){
    return "xd";
} 
console.log(function3());

// Ternary operator: ?
//condition ? ifTrue : ifFalse
//a shortcut for if else statement

x>7 ? console.log("xd") : console.log("not xd");

// let = variables limited to block scope (Can't escape any block)
// var = variables limited to function scope(Only can't escape a function) 
// For example, if you define in a for loop, it will be global unlike let
// And if it's global, it can change browser's window properties
// which may be dangerous

//Template literals (` `) instead of single or double quotes (ASCII 96)

console.log(`${myNumber1} ${myVariable2}`);

let myString3 =
`This  is a multiline string
browser will show line by line
${myNumber1}`;
console.log(myString3);

let myNumber2 = 123456.789;
let myNumber3 = 0.1
console.log(myNumber2.toLocaleString("en-US"));
console.log(myNumber2.toLocaleString("tr-TR"));
console.log(myNumber2.toLocaleString("en-US", {style: "currency", currency: "USD"}));
console.log(myNumber2.toLocaleString(undefined, {style: "percent"}));
console.log(myNumber3.toLocaleString(undefined, {style: "percent"}));
console.log(myNumber2.toLocaleString(undefined, {style: "unit", unit: "celsius"}));
console.log(myNumber2.toLocaleString(undefined, {style: "unit", unit: "meter"}));
//undefined sets browser default

let myArray1 = ["Element1","Element2","Element3"];

myArray1.push("Element4");      //Adds element to the end
myArray1.unshift("Element0");   //Adds element to the beginning
console.log(myArray1);
myArray1.pop();                 //Removes the last element
myArray1.shift();               //Removes the first element
console.log(myArray1);
console.log(myArray1.length);
console.log(myArray1.indexOf("Element2"));
console.log(myArray1.indexOf("FakeElement")) // Elements do not exist returns -1
console.log(myArray1[9]); //Index out of range returns undefined

for (let i of myArray1) {
    console.log(i);
}

myArray1.forEach(element => {   //Can be used in the form of
    console.log(element);       //myArray1.forEach(aCallbackFunc)
});

for (let i = myArray1.length - 1; i >= 0; i--){
    console.log(myArray1[i]);
}

let myArray2 = ["tangerine","apple","lemon","strawberry"];

function capitalizeAndPrint(element){
    console.log(element[0].toUpperCase()+ element.substring(1));
}
//For-each method applies element, index and array, but we do
//not have to pass any of them.
function capitalizeAndAssign(element,index,array){
    array[index] = element[0].toUpperCase()+ element.substring(1);
}
myArray2.forEach(capitalizeAndPrint);
console.log(myArray2.sort().reverse());
console.log(myArray2); //These methods mutates actual array

let myArray3 = [7,23,4,5,33,-67,51];

console.log(myArray3.sort()); //Sorts alphabetically
console.log(myArray3.sort(function (a,b) {return a-b;})); //sorts numerically

let myArray4 = [myArray1,myArray2,myArray3];

console.log(myArray4);
console.log(myArray4[1][2]);

console.log(...myArray2); // Spread (unpacking) operator 
console.log(..."    Hi! This is a text.");

function function4(x, y, ...args){ //packing operator 
    return 0 //A for loop can be used to iterate over the args ARRAY
}

/*Functions passed as an argument to another function
are called "callback". We do not call 
(using parantheses at the end of the function's name) 
the callback while passing. Instead, we call it in the 
function.This ensures the callback is not gonna run before
a task is completed which helps us develop asynchronous
code and avoid errors and potential problems*/

let myString4 = "This is a test string";

console.log(myString4.substring(5,9));  //(inclusive-exclusive)
console.log(myString4.substring(10));   //single value is start value

function capitalizeAndReturn(element){
    return element[0].toUpperCase()+ element.substring(1);
}

console.log(myArray2);
console.log(myArray2.map(capitalizeAndReturn));
console.log(myArray2);
//Map function creates a new array to append the returned values
//If there is no returned value, assigns to that index "undefined"
//Foreach method does not use returned values

function measureLength(element){
    return element.length > 5;
}

console.log(myArray2.filter(measureLength));
//creates a new array with the elements that returns true when
//passed the callback function

let myArray5 = [5, 10, 15, 20, 25, 30];

function  additionWithList(total,element){
    console.log(`The total is ${total}.`);
    console.log(`The element is ${element}.`);
    console.log(""); //Shortest way of doing this
    return total+element;
}

console.log(myArray2.reduce(additionWithList));
//reduce function reduces an element to a single value
//does not return an array,returns string, number etc.

//function expressions (anonymous functions) helps us to
//avoid polluting global scope with function names

//Arrow functions compact the code and make it more readable
let arrowFunc1 = (x,y) => { 
    console.log(x-y);
    return x+y;
}
//Curly braces are not needed when there is only 1 line of expression
//Parantheses are not needed when there is only 1 parameter
//Curly braces always needed while using anonymous functions.
console.log(`${arrowFunc1(45,34)}`)

const myMap1 = new Map([
    ["key1",10],
    ["key2",20],
    ["key3",30],
    ["key4",40]
]);

console.log(myMap1.get("key1"));
myMap1.delete("key1");
myMap1.set("key5",50); //Do not use square brackets here
console.log(myMap1.values()); //Return type is MapIterator, 
console.log(myMap1.entries()); //not array
console.log(myMap1.has("key3"));
console.log(myMap1.size);
myMap1.forEach((v,k) => console.log(`Key: ${k}\t Value: ${v}`));
//Pay attention^^^^^^HERE. It's not k, v.

const myObject1 = {
    property1:"value1",
    property2:20,
    property3:true,
    
    method1 : function(){
        console.log("You called the method1.");
        console.log(`property2 is: ${this.property2}`);
    },
    method2 : function(){
        console.log("You called the method2.");
        console.log(`property3 is: ${this.property3}`);
    }
}

myObject1.property1 = "xd"

console.log(myObject1.property1);

myObject1.method1();

//this.name = "myWindow";
console.log(this); //Our immediate context is the window currently

//const keyword does not makes the value immutable, it just
//prevents reassigning a different value to the variable

class MyClass1{
    property0 = 0;
    static numberObjects = 0;

    constructor(property1, property2){
        this._property1 = property1;
        this.property2 = property2;
        MyClass1.numberObjects+=1;
    }

    method1 = function(){
        console.log(`You called method1 with ${this._property1}.`);
    }

    static method2 = function(){
        console.log("This is a static method.");
    }

    get property1(){
        return this._property1;
    }
    set property1(value){
        if (value > 20) {
            value = 20;
        }
        else if (value < 0){
            value = 0;
        }
        this._property1 = value;
    }
}

const object1 = new MyClass1(10,"value1");
const object2 = new MyClass1(10,"value1");
const object3 = new MyClass1(10,"value1");
const object4 = new MyClass1(10,"value1");

console.log(MyClass1.numberObjects);
object1.property0 +=1;
MyClass1.method2();
object1.property1 = 1000000; //We do not have access to _property1.
//Nevertheless, we can access it by object1._property1,
//but people will know they should not do
console.log(object1.property1);
console.log(object1.property1);

class ChildClass1 extends MyClass1{
    childProperty1 = 5;

    constructor(property1){
        super(property1);
    }

    childMethod1 = function(){
        console.log("You called child method.");
    }
}

const childObject1 = new ChildClass1(50);

console.log(childObject1.property2);
console.log(childObject1.property0);
console.log(childObject1.property1);
childObject1.method1();
childObject1.property1 = 500; //set method is working
console.log(childObject1.property1);

object1.property1 = 500;
console.log(object1.property1);
//It's not possible to call getters and setters as function
//in JS. If there is no setter, you cannot mutate unless you
//use _property which you shouldn't. If there are both of them
//you can access normally.

//In JavaScript, you can call function before the definition.
const myArray6 = new Array();
for (let i = 100; i < 160; i = i+10) {
    myArray6.push(new ChildClass1(i));
}
console.log(myArray6);

//Errors are objects in javascript
try {
    //let x = window.prompt("Please enter a number.");
    x = Number(x);
    console.lag();
    throw new Error("Something went wrong");
    if (isNaN(x)) throw "This is not a number!";
    //When error is occured either via throw keyword or
    //in other ways, rest of the try block is not executed.
}
catch (error) {
    console.log(error);
}
finally{
    console.log("This will be executed always.");
}

function function5(x, y){
    console.log("This is the first alert.");
}
/*setTimeout() invokes a function after a number of miliseconds.
This is an asynchronous function, so does not stop normal 
execution, continues as a thread.*/ 
/*setTimeout(function5, 3000, "arg1", "arg2");
const myTimer1 = setTimeout(() => console.log("This is the second alert!"), 6000);
//setTimeout(function() {alert("Do something! This is the third alert")}, 9000)
if (true){
    clearTimeout(myTimer1); //Stops the timer completely.
}*/

/*setInterval() invokes a function repeatedly after a number of
miliseconds, this is also an asynchronous function. */

/*const myTimer2 = setInterval(myFunction6, 1000);
let timer = 10
function myFunction6(){
    console.log(timer);
    timer--;
    if (timer ==0){
        clearInterval(myTimer2);
    }
}*/
/*let counter = 5
while (counter<500){
    console.log("counter");
    counter++;
}*/

console.time("Timer1");

console.log("");
let myDate1 = new Date();
myDate1.setFullYear(2000);
let myString5 = `
${myDate1}
${myDate1.getFullYear()}
${myDate1.getDate()} //Day of Month
${myDate1.getDay()} //Day of week
${myDate1.getMilliseconds()}
${myDate1.toLocaleString()}
${myDate1.toLocaleDateString()}
${myDate1.toLocaleTimeString()}
${myDate1.toUTCString()}
${new Date(0)} //Epoch
${new Date(1000)} //Miliseconds after Epoch
${new Date(0, 0, 1, 0, 0, 0, 999)}
`;

console.log(myString5);

let myValue2 = 0 || 100 || 132231;
console.log(myValue2); 
/*If the first element of a or operation returns true, variable
will be assigned directly to this value.If it returns false,
it will be assigned to the other one even if it returns false,
If there is more than 2, the other values will be checked 
whether they returns true*/
/* && operator will assign to the first value which returns
false. If all of them returns true, it will assign to the 
last one.*/
/* ^ operator will return the binary operation result*/

console.timeEnd("Timer1");
// Each timer has a unique name. Time will be printed
// automatically when you invoke console.timeEnd()
// Only measures the synchronous code, does not include
// threads' times

let myPromise1 = new Promise((resolve, reject) => {
    let asynchronousOperationSuccessful = false;

    if(asynchronousOperationSuccessful){
        resolve("Operation successful!");
    }    //This string is the return value
    else{
        reject("Operation failed.");
    }
}); //This is the producing part of the promise
// Asynchronous operations have state "pending" (waiting) firstly
// Then the state turns into either "fulfilled" or "rejected"

myPromise1.then(value => console.log(value)).catch(error => console.log(error));
//This is the consuming part of the promise which will be 
//invoked only if promise is resolved

//reject does not neccessarily needed
let myPromise2 = time=> new Promise(resolve => {
    setTimeout(resolve,time);
});
myPromise2(3000).then(() => console.log("You waited for 3 seconds."));

//Promises let asynchronous methods return values like 
//synchronous methods.

//async makes a function return a Promise (Producing part)
//await makes a function wait for a Promise (Consuming part)

async function equalsMyPromise1(){
    let asynchronousOperationSuccessful1 = false;

    if(asynchronousOperationSuccessful1){
        return "Operation successful!";
    }   //Instead of resolve
    else{
        throw "Operation failed.";
    }   //Instead of reject
}
equalsMyPromise1().then(value => console.log(value)).catch(error => console.log(error));
//We need to use parantheses to call function unlike Promise
//Instead of using async here, we can return and throw 
//Promise.resolve("Operation successful!") and
//Promise.reject("Operation failed.") respectively

//await keyword is only valid in async functions 

async function function7(){
    try{
        console.log(await equalsMyPromise1());
    }
    catch(error){
        console.log(error);
    }
}
function7();

import * as myUtils from "./JSModule2.js";
//Second import syntax
console.log(myUtils.getCircumference(8));

//Document Object Model (DOM)
//An interface for changing the content of a page
console.log(document);
console.log(document.URL);
console.log(document.title);
document.title = "JS Title";
console.log(document.title);
document.body.style.backgroundColor = "orange";
console.log(document.getElementsByName("Options1"));
console.log(document.getElementsByName("Options1")[1]);
console.log(document.querySelector("#button1"));
//Using querySelector method, we can search for ids(#),classes(.), 
//attributes([]) (like "for" attribute) and tags(does not have 
//any mark), but it will return only the first element it finds. 
//To find all, we have to use querySelectorAll() method

let myBody = document.body;

console.log(myBody.firstElementChild);
console.log(myBody.firstChild);
console.log(myBody.lastElementChild);
console.log(myBody.parentElement);
console.log(myBody.previousElementSibling);
console.log(myBody.children);
console.log(Array.from(myBody.children));

//To add/change HTML elements, .innerHTML or .textContent
//methods can be used, but former is vulnerable to XSS attacks
//so latter one is more secure

const header1 = document.createElement("h1");
const header2 = document.createElement("h1");
const paragraph1 = document.createElement("p");
header1.innerHTML = "This is h1 header.";
header2.innerHTML = "This is h1 header.";
header1.id = "header1";
paragraph1.textContent = "This is a paragraph."
myBody.append(header1);
myBody.prepend(header2);
myBody.insertBefore(paragraph1,myBody.getElementsByTagName("h1")[1]);

let paragraph2 = document.getElementById("paragraph2");

paragraph2.style.border = "3px solid black";
paragraph2.style.textAlign = "center";

myBody.onload = function8;
//we can set attributes in the HTML opening tags such as:
//<body onload="function8()".(We should call function here)

function function8(){
    myBody.style.backgroundColor = "lightblue";
}

let myTextBox1 = document.getElementById("input1");
myTextBox1.onchange = function9;
//To call this function, you should make a change and leave
//the box

function function9(){
    myTextBox1.style.borderRadius = "5px";
}

paragraph2.onmouseover = function10;
//If you do not set a onmouse levae function, orange will not
//change when you leave the box and will remain orange always
paragraph2.onmouseout = function11;
function function10(){
    this.style.backgroundColor = "orange";
}
function function11(){
    this.style.backgroundColor = "dodgerblue";
}

header1.style.border = "3px solid black";
header1.onmousedown = function12;
header1.onmouseup = function13;
function function12(){
    header1.style.borderRadius = "10px";
}
function function13(){
    header1.style.borderRadius = "3px";
}
header2.style.border = "3px solid black";

//Event listeners is used to handle multiple events.
header2.addEventListener("paste", function10);
header2.addEventListener("mouseover", function11);

const smallBox = document.getElementById("innerDiv");
const bigBox = document.getElementById("outerDiv");

smallBox.style.height = "100px";
smallBox.style.width = "100px";
bigBox.style.width = "200px";
bigBox.style.height = "200px";
smallBox.style.backgroundColor = "dodgerblue";
bigBox.style.backgroundColor = "black";

smallBox.addEventListener("click", function14);
bigBox.addEventListener("click", function14,true);
//Normally, when you click to innerDiv, it invokes the function
//first. However, if you set useCapture=true of outerDiv,
//outerDiv invokes first.

function function14(){
    alert(`You clicked on ${this.id}.`);
}
bigBox.style.float = "right";
header1.addEventListener("click",function15);
function function15(){
    if (bigBox.style.display === "none"){
        console.log(bigBox.style.display);
        bigBox.style.display = "block";
    }
    else{
        bigBox.style.display = "none";
    }
}

window.addEventListener("keydown", event => console.log(event.key));
//Displays all keys including special ones like F1, Enter, Shift
//and can print upper-lower cases.

/** @type {HTMLCanvasElement} */ /*To make VSCode recognize the canvas element, we need to add this type hint.*/
let canvas1 = document.getElementById("canvas1");
canvas1.height = 500;
canvas1.width = 500;
let context1 = canvas1.getContext("2d");
context1.beginPath();
context1.lineWidth = 5;
context1.strokeStyle = "orange";
context1.fillStyle = "slategrey";
context1.moveTo(0,0);
context1.lineTo(500,500);
context1.moveTo(0,0);
context1.bezierCurveTo(982,250,250,982,0,0);
context1.moveTo(50,450);
context1.arc(50,450,50,0,3*Math.PI/2,true); //First 2 values are the center coordinates
context1.stroke();
context1.fillRect(400,0,100,100);
context1.strokeRect(400,0,100,100);
context1.moveTo(250,0);
context1.arcTo(0,0,0,500,250);
context1.stroke();
context1.font = "50px MV Boli";
context1.fillStyle = "black";
context1.textAlign = "center";
context1.fillText("M",450,70,100);

canvas1.addEventListener("click", () => console.log(window.scrollX,window.scrollY))
console.log(window.location.href);
console.log(window.location.hostname);
console.log(window.location.pathname);

paragraph2.addEventListener("click", () => window.open("https://www.google.com/"));
//There is also a window,close() method to close current window
//and window.print() method to print current page
//window.alert() to display a text
//and window.confirm() to Ask a question with OK and cancel options
//window.prompt() to enter an input

//cookie = a small text file stored on your computer used to
//remember information about the user, saved in name=value pairs

console.log(navigator.onLine);
console.log(navigator.cookieEnabled);
console.log(document.cookie);