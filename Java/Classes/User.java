package Classes;

import java.io.Serializable;

public class User implements Serializable{

    //We can manually set serialVersionUID
    private static final long serialVersionUID = 1;

    String name;
    transient String password;
    public User(String name,String password) {
        this.name = name;
        this.password = password;
    }
    public String getName() {
        return this.name;
    }
    public String getPassword() {
        return this.password;
    }
}
