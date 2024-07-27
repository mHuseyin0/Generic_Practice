import java.awt.Color;
import java.awt.Font;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.border.Border;

public class Main7_JFrameBasics {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();
        JLabel myLabel = new JLabel();
        Border myBorder = BorderFactory.createLineBorder(Color.GREEN, 5, true);
        
        myFrame.setVisible(true);
        myFrame.setSize(1000,1000);
        myFrame.setTitle("THE FRAME");
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setResizable(true);
        //myFrame.setLayout(null); Cannot be used with pack().
        myFrame.getContentPane().setBackground(new Color(120,120,120));
        
        ImageIcon myLogo = new ImageIcon("Icon1.png");
        myFrame.setIconImage(myLogo.getImage());

        ImageIcon myImage = new ImageIcon("Icon7.jpg");
        myLabel.setIcon(myImage);

        myLabel.setText("Hello!");
        myLabel.setHorizontalTextPosition(JLabel.CENTER);
        myLabel.setVerticalTextPosition(JLabel.TOP);
        myLabel.setHorizontalAlignment(JLabel.CENTER);
        myLabel.setForeground(Color.RED);
        myLabel.setFont(new Font("MV Boli", Font.PLAIN, 70));
        myLabel.setIconTextGap(20);
        myLabel.setBackground(Color.black);
        myLabel.setOpaque(true);
        myLabel.setBorder(myBorder);
        //myLabel.setBounds(330, 75, 600, 600); Cannot be used with pack().

        myFrame.add(myLabel);
        myFrame.pack();
    }
}