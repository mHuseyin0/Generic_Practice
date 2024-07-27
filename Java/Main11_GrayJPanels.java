import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

import java.awt.Color;
import java.awt.GridLayout;
import java.util.HashMap;

public class Main11_GrayJPanels {
    public static void main(String[] args) {

        JFrame myFrame = new JFrame();
        myFrame.setSize(400, 400);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setBackground(Color.black);
        myFrame.setLayout(new GridLayout(5, 5, 20, 20));

        HashMap<Integer,JPanel> hashMap = new HashMap<>();
        HashMap<Integer,JButton> hashMap2 = new HashMap<>();

        for (Integer i = 0; i < 6; i++) {
            hashMap.put(i, new JPanel());
            hashMap.get(i).setBackground(new Color((int)(i*16),(int)(i*16),(int)(i*16)));
            myFrame.add(hashMap.get(i));

            if (i == 0) {
                hashMap.get(0).setLayout(new GridLayout(3,3,10,10));
                for ( Integer in = 0; in < 9; in++) {
                    hashMap2.put(in, new JButton());
                    hashMap.get(0).add(hashMap2.get(in));
                }
            }
        }
        myFrame.setVisible(true);
    }
}
