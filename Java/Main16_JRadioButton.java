import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JRadioButton;

public class Main16_JRadioButton {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();

        JRadioButton myRadioButton1 = new JRadioButton("Option 1");
        JRadioButton myRadioButton2 = new JRadioButton("Option 2");
        JRadioButton myRadioButton3 = new JRadioButton("Option 3");

        JButton myButton = new JButton("Select");
        myButton.setFocusable(false);

        ButtonGroup myGroup = new ButtonGroup();
        myGroup.add(myRadioButton1);
        myGroup.add(myRadioButton2);
        myGroup.add(myRadioButton3);

        ImageIcon myIcon1 = new ImageIcon("Icon2.jpg");

        ImageIcon myIcon2 = new ImageIcon("Icon3.jpg");

        myRadioButton1.setFocusable(false);
        myRadioButton2.setFocusable(false);
        myRadioButton3.setFocusable(false);

        myRadioButton1.setIcon(myIcon2);
        myRadioButton2.setIcon(myIcon2);
        myRadioButton3.setIcon(myIcon2);

        myRadioButton1.setSelectedIcon(myIcon1);
        myRadioButton2.setSelectedIcon(myIcon1);
        myRadioButton3.setSelectedIcon(myIcon1);
        
        myButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed (ActionEvent e) {
                if (e.getSource() == myButton) {
                    if (myRadioButton1.isSelected()) {
                        System.out.println("You picked up option 1.");
                    }
                    if (myRadioButton2.isSelected()) {
                        System.out.println("You picked up option 2.");
                    }                    
                    if (myRadioButton3.isSelected()) {
                        System.out.println("You picked up option 3.");
                    }
                    myButton.setEnabled(false);
                    myRadioButton1.setEnabled(false);
                    myRadioButton2.setEnabled(false);
                    myRadioButton3.setEnabled(false);
                }
            } 
        });

        myFrame.add(myRadioButton1);
        myFrame.add(myRadioButton2);
        myFrame.add(myRadioButton3);
        myFrame.add(myButton);

        myFrame.getContentPane().setBackground(Color.black);
        myFrame.setLayout(new FlowLayout());
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.pack();
        myFrame.setResizable(false);
        myFrame.setVisible(true);
    }
}
