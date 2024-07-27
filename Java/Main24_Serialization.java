import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.io.ObjectStreamClass;

import Classes.User;

public class Main24_Serialization {
    public static void main(String[] args) throws IOException {
        User user1 = new User("User1", "xd1");

        FileOutputStream fileOut = new FileOutputStream("UserInfo.ser");
        ObjectOutputStream out = new ObjectOutputStream(fileOut);
        out.writeObject(user1);
        fileOut.close();
        out.close();

        //Serialization and deserialization need to have the same serialVersionUID to work
        //Only the exact same classes have the same serialVersionUID
        long serialVersionUID = ObjectStreamClass.lookup(user1.getClass()).getSerialVersionUID();
        System.out.println(serialVersionUID);
    }
}
