import java.sql.*;
public class Main29_MySQL {
    public static void main(String[] args) {
        String dbURL = "jdbc:mysql://localhost:3306/db1";
        String javaURL = "jdbc:mysql://localhost:3306/java";
        String user = "root";
        String password = "admin";

        try {
            Connection connection = DriverManager.getConnection(dbURL, user, password);
            Statement statement = connection.createStatement();
            statement.executeUpdate("CREATE DATABASE IF NOT EXISTS java");
            ResultSet result = statement.executeQuery("SELECT * FROM aminoacids");
            // Initially placed before first row

        while(result.next()){ // Moves forward one row and returns true if there are more rows to process
                System.out.printf("%-3s", result.getString("number") + "-");
                System.out.printf("%-20s", result.getString("name"));
                System.out.printf("%-10s", result.getString("molecularWeight"));
                System.out.printf("%-20s", result.getString("molecularFormula"));
                System.out.println();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
        System.out.println();
        try {
            Connection connection = DriverManager.getConnection(javaURL, user, password);
            Statement statement = connection.createStatement();
            statement.executeUpdate("CREATE TABLE IF NOT EXISTS test (column1 INT, column2 VARCHAR(50))");
            //statement.executeUpdate("INSERT INTO test (column1, column2) VALUES (1, 'element1'), (2, 'element2')");
            // Deleting something from a table with executeUpdate() function returns number of rows affected as int.
            ResultSet result = statement.executeQuery("SELECT * FROM test");

            displayData(result);

        } catch (Exception e) {
            System.out.println(e);
        }
        System.out.println();
        try {
            Connection connection = DriverManager.getConnection(javaURL, user, password);
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM test WHERE column1 = ?");
            statement.setInt(1, 1); // Indexing question marks starts from 1 (first 1), value of question mark is the second
            ResultSet result = statement.executeQuery();
            displayData(result);
        } catch (Exception e) {
            System.out.println(e);
        }
        System.out.println();
        try {
            Connection connection = DriverManager.getConnection(dbURL, user, password);
            CallableStatement statement = connection.prepareCall("{CALL updateElementUpdater()}");
            statement.execute();
   
        } catch (Exception e) {
            System.out.println(e);
        }
        try{
            Connection connection = DriverManager.getConnection(dbURL, user, password);
            CallableStatement statement = connection.prepareCall("SELECT elementLocation(?, ?) AS number");
            statement.setString(1, "O");
            statement.setString(2, "C6H12O6");
            ResultSet result = statement.executeQuery();
            while (result.next()) {
                System.out.println(result.getInt("number"));
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
    public static void displayData(ResultSet result){
        try{
            while (result.next()) {
                System.out.println(result.getString("column1") + "-" + result.getString("column2"));
            }
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}
