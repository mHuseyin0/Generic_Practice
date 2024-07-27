import javax.swing.JOptionPane;

public class Main13_JOptionPaneFeatures {
    public static void main(String[] args) {
        
        JOptionPane.showMessageDialog(null,"Hello!","Greeting",JOptionPane.PLAIN_MESSAGE);

        int answer = JOptionPane.showConfirmDialog(null, "Do you want to exit?", "Quit", JOptionPane.YES_NO_CANCEL_OPTION);
        // Yes = 0 , No = 1 , Cancel = 2

        String name = JOptionPane.showInputDialog("What is your name?");
        System.out.println(name);

        String[] options = {"Stay","Exit","I don't know","Wait"};

        answer = JOptionPane.showOptionDialog(null, "What do you want to do?", "Choice", JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, 0);
        System.out.println(answer);
   }
}
