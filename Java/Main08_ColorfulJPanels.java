import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Main8_ColorfulJPanels {
    public static boolean colorChanger = true;
    public static void main(String[] args) {
        
        int margin = 100;
        int unit = 150;

        ArrayList<Color> myColors = new ArrayList<>();

        myColors.add(Color.green);
        myColors.add(Color.darkGray);
        myColors.add(Color.orange);
        myColors.add(Color.red);
        myColors.add(Color.lightGray);
        myColors.add(Color.yellow);
        myColors.add(Color.magenta);
        myColors.add(Color.green);
        myColors.add(Color.darkGray);
        myColors.add(Color.orange);
        myColors.add(Color.red);
        myColors.add(Color.lightGray);
        myColors.add(Color.yellow);
        myColors.add(Color.magenta);

        JFrame myFrame = new JFrame();
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setLayout(null);
        myFrame.setSize(1365, 767);
        myFrame.getContentPane().setBackground(Color.BLACK);

        ImageIcon myIcon = new ImageIcon("Icon2.png");

        JLabel myLabel = new JLabel();
        myLabel.setText("Have a nice day!");
        myLabel.setForeground(Color.black);
        myLabel.setFont(new Font("Harlow Solid Italic", Font.PLAIN, 20));
        myLabel.setIcon(myIcon);
        myLabel.setHorizontalAlignment(JLabel.CENTER);
        myLabel.setVerticalAlignment(JLabel.CENTER);
        myLabel.setVerticalTextPosition(JLabel.TOP);
        myLabel.setHorizontalTextPosition(JLabel.CENTER);

        JPanel myPanel1 = new JPanel();
        myPanel1.setBounds(margin, margin, unit, unit);

        JPanel myPanel2 = new JPanel();
        myPanel2.setBounds(margin+unit, margin, unit, unit);

        JPanel myPanel3 = new JPanel();
        myPanel3.setBounds(margin+2*unit, margin, unit, unit);

        JPanel myPanel4 = new JPanel();
        myPanel4.setBounds(margin+3*unit, margin, 2*unit, 2*unit);

        JPanel myPanel5 = new JPanel();
        myPanel5.setBounds(margin+5*unit, margin, unit, unit);  
        
        JPanel myPanel6 = new JPanel();
        myPanel6.setBounds(margin+6*unit, margin, unit, unit);

        JPanel myPanel7 = new JPanel();
        myPanel7.setBounds(margin+7*unit, margin, unit, unit);

        JButton myButton = new JButton();
        myButton.setBounds((int)(margin+3.75*unit), margin/4, margin/2, margin/2);
        
        myPanel4.add(myLabel);
        myFrame.add(myPanel1);
        myFrame.add(myPanel2);
        myFrame.add(myPanel3);
        myFrame.add(myPanel4);
        myFrame.add(myPanel5);
        myFrame.add(myPanel6);
        myFrame.add(myPanel7);
        myFrame.add(myButton);
        
        myButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (e.getSource() == myButton && colorChanger) {
                    colorChanger = false;
                }
                else if (e.getSource() == myButton && !colorChanger) {
                    colorChanger = true;
                }
            }
        });
        myFrame.setVisible(true);
        int i = 7;
        while (true) {
            if (colorChanger) {
                myPanel1.setBackground(myColors.get(i));
                myPanel2.setBackground(myColors.get(i+1));
                myPanel3.setBackground(myColors.get(i+2));
                myPanel4.setBackground(myColors.get(i+3));
                myPanel5.setBackground(myColors.get(i+4));
                myPanel6.setBackground(myColors.get(i+5));
                myPanel7.setBackground(myColors.get(i+6));
                i--;
            
                if (i == 0) {
                    i = 7;
                }

                try{
                    TimeUnit.SECONDS.sleep(1);
                } catch (Exception e) {
                }
            }
            System.out.print(""); //No idea why this makes the code work.
        } 
    }
}