import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;

class MyFrame extends JFrame implements ActionListener {
    
    public JButton myButton;

    public MyFrame() {
        this.setLayout(new FlowLayout());
        this.setSize(100, 100);
        
        myButton = new JButton("Select File");
        myButton.addActionListener(this);
        myButton.setFocusable(false);
        
        this.add(myButton);
        this.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == myButton) {
            
            JFileChooser myFileChooser = new JFileChooser();

            myFileChooser.setCurrentDirectory(new File("."));

            int response = myFileChooser.showSaveDialog(null);
            response = myFileChooser.showOpenDialog(null);

            if (response == JFileChooser.APPROVE_OPTION) {
                File myFile = new File(myFileChooser.getSelectedFile().getAbsolutePath());
                System.out.println(myFile);
            }
        }
    }

    
}

public class Main18_JFileChooser {
    public static void main(String[] args) {
        MyFrame newMyFrame = new MyFrame();
        newMyFrame.setDefaultCloseOperation(MyFrame.EXIT_ON_CLOSE);
    }
}
