import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.util.HashMap;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main10_AnonymousObjects {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();
        myFrame.setSize(400, 400);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setLayout(new FlowLayout(FlowLayout.LEFT, 20, 10));

        JPanel myPanel1 = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        JPanel myPanel2 = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        
        myPanel1.setPreferredSize(new Dimension(200, 125));
        myPanel2.setPreferredSize(new Dimension(200, 125));

        myPanel1.setBackground(Color.darkGray);
        myPanel2.setBackground(Color.darkGray);
        
        int buttonSize = 40;

        int totalButtonNum = 14;

        HashMap<Integer,JButton> myButtons = new HashMap<Integer,JButton>();

        for (int buttonNum = 0; buttonNum < totalButtonNum; buttonNum++) {
            myButtons.put(buttonNum, new JButton());
            if (buttonNum < totalButtonNum/2) {
                myPanel1.add(myButtons.get(buttonNum));
            } 
            else {
                myPanel2.add(myButtons.get(buttonNum));
            }
            ((JButton)myButtons.get(buttonNum)).setPreferredSize(new Dimension(buttonSize, buttonSize));
        }

        myFrame.add(myPanel1);
        myFrame.add(myPanel2);

        myFrame.setVisible(true);  
    }
}
