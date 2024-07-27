import javax.swing.JOptionPane;

public class Main2_JOptionPane {
        public static void main(String[] args) {
        
            String inputName=JOptionPane.showInputDialog("Please enter your name:");
            JOptionPane.showMessageDialog(null,"Hello "+ inputName);

            int inputAge=Integer.parseInt(JOptionPane.showInputDialog("Please enter your age:"));
            JOptionPane.showMessageDialog(null,"Your age is "+ inputAge);

    }
}
