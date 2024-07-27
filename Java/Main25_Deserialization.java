import java.io.*;
import Classes.*;

public class Main25_Deserialization{
    public static void main(String[] args) throws IOException, ClassNotFoundException{
        User user = null;
        FileInputStream fileIn = new FileInputStream("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\UserInfo.ser");
        ObjectInputStream in = new ObjectInputStream(fileIn);
        user = (User) in.readObject();
        in.close();
        fileIn.close();
        System.out.println(user.getName());
        System.out.println(user.getPassword()); 

        long serialVersionUID = ObjectStreamClass.lookup(user.getClass()).getSerialVersionUID();
        System.out.println(serialVersionUID);
    }
}
