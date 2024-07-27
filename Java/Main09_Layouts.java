import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.util.HashMap;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main9_Layouts {
    public static void main(String[] args) {
         
        JFrame myFrame = new JFrame();
        myFrame.setSize(900,900);
        myFrame.setLayout(new BorderLayout(10,10));
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel myPanel1 = new JPanel();
        JPanel myPanel2 = new JPanel();
        JPanel myPanel3 = new JPanel();
        JPanel myPanel4 = new JPanel();
        JPanel myPanel5 = new JPanel();

        myPanel1.setPreferredSize(new Dimension(100,500));
        myPanel2.setPreferredSize(new Dimension(100,100));
        myPanel3.setPreferredSize(new Dimension(100,100));
        myPanel4.setPreferredSize(new Dimension(100,100));
        myPanel5.setPreferredSize(new Dimension(100,100));

        myPanel1.setBackground(Color.red);
        myPanel2.setBackground(Color.green);
        myPanel3.setBackground(Color.blue);
        myPanel4.setBackground(Color.yellow);
        myPanel5.setBackground(Color.black);

        myFrame.add(myPanel1,BorderLayout.WEST);
        myFrame.add(myPanel2,BorderLayout.NORTH);
        myFrame.add(myPanel3,BorderLayout.EAST);
        myFrame.add(myPanel4,BorderLayout.SOUTH);
        myFrame.add(myPanel5,BorderLayout.CENTER);

        myPanel5.setLayout(new BorderLayout(5,5));

        JPanel myPanel6 = new JPanel();
        JPanel myPanel7 = new JPanel();
        JPanel myPanel8 = new JPanel();
        JPanel myPanel9 = new JPanel();
        JPanel myPanel10 = new JPanel();
        
        myPanel6.setBackground(Color.white);
        myPanel7.setBackground(Color.lightGray);
        myPanel8.setBackground(Color.white);
        myPanel9.setBackground(Color.darkGray);
        myPanel10.setBackground(Color.gray);

        myPanel10.setLayout(new GridLayout(3,3,30,30));
        HashMap<Integer,JButton> hashMap = new HashMap<>();
        for (Integer i = 0; i < 9; i++) {
            hashMap.put(i, new JButton());
            myPanel10.add(hashMap.get(i));
        }


        myPanel6.setPreferredSize(new Dimension(100,500));
        myPanel7.setPreferredSize(new Dimension(100,100));
        myPanel8.setPreferredSize(new Dimension(100,100));
        myPanel9.setPreferredSize(new Dimension(100,100));
        myPanel10.setPreferredSize(new Dimension(100,100));

        myPanel5.add(myPanel6,BorderLayout.WEST);
        myPanel5.add(myPanel7,BorderLayout.NORTH);
        myPanel5.add(myPanel8,BorderLayout.EAST);
        myPanel5.add(myPanel9,BorderLayout.SOUTH);
        myPanel5.add(myPanel10,BorderLayout.CENTER);

        
        myFrame.setVisible(true);
    }
}