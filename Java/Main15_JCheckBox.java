import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JCheckBox;
import javax.swing.JFrame;

public class Main15_JCheckBox {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();

        ImageIcon myIcon1 = new ImageIcon("Icon3.jpg");

        ImageIcon myIcon2 = new ImageIcon("Icon2.jpg");

        JCheckBox myCheckBox = new JCheckBox("I am not a robot.", false);
        myCheckBox.setFocusable(false);
        myCheckBox.setIcon(myIcon1);
        myCheckBox.setSelectedIcon(myIcon2);
        myCheckBox.setBackground(Color.cyan);
        myCheckBox.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (e.getSource() == myCheckBox) {
                    System.out.println(myCheckBox.isSelected());
                }
            }
        });

        myFrame.add(myCheckBox);
        myFrame.getContentPane().setBackground(Color.black);
        myFrame.setLayout(new FlowLayout(FlowLayout.LEADING));
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.pack();
        myFrame.setResizable(false);
        myFrame.setVisible(true);
    }
}
