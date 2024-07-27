<?php
    echo"This is written by PHP <br>";

    $name = "xd";
    echo$name;
    echo"<br>Name: {$name}<br>";

    $age = 30;
    echo"Age: {$age}<br>";

    $bool1 = false;
    $bool2 = true;
    echo"Bool1 (true) = {$bool1}<br>";
    echo"Bool2 (false)= {$bool2}<br>";

    $bool1ORbool2 = null;
    echo"Bool1 OR Bool2 = ";
    $bool1ORbool2 = $bool1 || $bool2;
    echo$bool1ORbool2 . "<br>";

    echo"Entered username = {$_GET["username"]} <br>";
    echo"Entered password = {$_GET["password"]} <br>";
    /* POST should be used in order not to display username and
     * password in the URL.
     */

    // Math function can be used directly (PI can be get with pi() fucntion)
    $randNum = rand(1,6);
    echo"Random number = {$randNum}<br>";

    // Escape character is backslash (/). Dollar sign must be printed using an escape character

    $figures = array(0,1,2,3,4,5,6,7,8);
    foreach ($figures as $figure){
        echo"Figures {$figure}: {$figure}<br>";
    }
    array_push($figures, 9);
    // array_pop() method removes the last element in place
    // array_shift() method removes the first element in placek
    // array_reverse() returns a reversed array to be assigned
    // count() method returns the numberof elements

    // Associative array
    $numbers = array(
                    1 => 10,
                    2 => 20,
                    3 => 30,
                    4 => 40,
                    5 => 50);
    $numbers[10] = 100;
    // array_keys() returns an array containing keys
    // array_values() returns an array containing values
    // array_flip() returns an array where keys and values flipped
    // pop, shift, count, reverse methods are available for associative arrays

    foreach ($numbers as $key => $value){
        echo"Key: {$key} => Value: {$value}<br>";
    }

    // isset() = Returns TRUE if a variable is declared and not null
    // empty() = Returns TRUE if a variable is not declared, false, null, ""

    // if(isset($_POST["submit"])) can be used to do something when a button is pressed
    // empty($POST["checkbox"]) returns true when a checkbox is not marked

    /* Naming a group of checkboxes like "checkboxes[]" in HTML and getting them in PHP like
     * $preferences = $_POST["checkboxes"]; returns an array containing their values
     * and assigns it to a variable. (Values are strings next to the checkboxes, not true or false)
     */

    function printFunction($firstArg, int $restrictedArg1, float $restrictedArg2){
        echo"{$firstArg} was passed to this function.<br>";
        return true;
    }

    printFunction("xd", 3, 5);

    /*
     * strtoupper(), strtolower(), trim(), str_pad() (fills a string with a character in a specified length)
     * str_replace(), str_shuffle(), strrev(), strcmp() (compares two strings), strlen(), strpos() )(indexOf),
     * substr(), explode() (returns an array containing words seperated with whitespaces), implode()
     * (reverse of explode), are useful string methods.
     */

    /* filter_input(INPUT_POST, "username", FILTER_SANITIZE_SPECIAL_CHARS) returns value of a form after omitting
     * special characters. It's better to do that in order not to allow user execute some code using forms.
     * FILTER_SANITIZE_NUMBER_INT omits everything except numbers. INPUT_GET must be used i we are using GET method
     * FILTER_SANITIZE_EMAIL filters all characters that is illegal for an email. FILTER_VALIDATE_INT returns the number
     * if a number is passed, otherwise returns "". empty() method can be used to check. There are other FILTER_VALIDATE
     * and FILTER_SANITIZE options
     */

    // include("header.html") function can be used to reuse content of a file (php, html, txt) in php

    // cookie = Information about a user stored in a user's web-browser
    // targeted advertisements, browsing preferences, and other non-sensitive data

    // setcookie("nameOfTheCookie", "valueOfTheCookie", time() + (86400 * 1), "/file/path/to/store/cookie")
    // creates a cookie to expire after a day. 86400 is seconds in a day. time() - 0 deletes the cookie
    // $_COOKIE returns an associative array of key-value pairs of cookies
    // isset can be used to know whether a cookie is set or not
    // F12 screen displays the current cookies

    // startsession() method starts a session. We have to use it in every PHP file to access session values
    // session_destroy() method terminates the sesion
    // We can store any key-value pairs about the session in $_SESSION like $_SESSION["username"] = "user1";

    // header("Location: home.php") function redirects the user to another page

    // $_SERVER stores all key-value pairs containing nearly all the thing needed.
    // $_SERVER["PHP_SELF"] returns the current page to navigate
    // $_SERVER["REQUEST_METHOD"] returns request method of the current page

    // password_hash($password, PASSWORD_DEFAULT) returns the hashed password

    // password_verify($password, $hashedPassword) returns true if the password inputted by used matches the
    // hashed password in the server

    // mysqli_connect() returns the connection to the database whose arguments are passed. It's better to use
    // try catch block. mysqli_close($connection) terminates it
    // localhost/phpmyadmin URL displays the database

    // $result = mysqli_query($connection, $command) implements a mysql syntax to a database. $command is the pure mysql
    // syntax here. Again try-catch block are useful. mysqli_num_rows($result) might be used in order to get row number
    // if we SELECTed some rows. mysqli_fetch_assoc($result) returns the next row as an associative array
    // while ($row = mysqli_fetch_assoc($result)) can be used to iterate over multiple rows.


?>

<html lang="en">
    <body>
        <p>
            This is written my HTML.
        </p>

        <form action="index.php" method="get">
            <label>Username: </label>
            <input type="text" placeholder="Username" name="username">
            <br>
            <label>Password: </label>
            <input type="text" placeholder="Password" name="password">
            <br><br>
            <input type="submit" value="Log in">
        </form>

    </body>
</html>