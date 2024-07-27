import java.awt.Color;
import java.util.HashMap;

import javax.swing.JFrame;
import javax.swing.JLayeredPane;
import javax.swing.JPanel;

public class Main12_LayeredPaneAndColorSpectrum {
    public static void main(String[] args) {
        
        JFrame myFrame = new JFrame();
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setSize(706,706);
        myFrame.setBackground(Color.white);
        myFrame.setLayout(null);

        JLayeredPane myLayeredPane = new JLayeredPane();
        myLayeredPane.setOpaque(true);
        myLayeredPane.setBounds(0, 0, 1360, 706);
        myLayeredPane.setBackground(Color.black);

        JPanel myPanel1 = new JPanel();
        JPanel myPanel2 = new JPanel();
        JPanel myPanel3 = new JPanel();

        myPanel1.setBounds(525,525,150,150);
        myPanel2.setBounds(575,475,150,150);
        myPanel3.setBounds(625,425,150,150);

        myPanel1.setBackground(Color.red);
        myPanel2.setBackground(Color.green);
        myPanel3.setBackground(Color.blue);

        myLayeredPane.add(myPanel1, Integer.valueOf(1));
        myLayeredPane.add(myPanel2, Integer.valueOf(0));
        myLayeredPane.add(myPanel3, Integer.valueOf(2));

        myFrame.add(myLayeredPane);

        HashMap<Integer,JPanel> hashMap = new HashMap<>();

        int phase = 1;
        int r = 1;
        int g = 1;
        int b = 1;

        Color myColor;

        for (Integer i = 0; i < 1500; i++) {
            myColor = new Color(r,g,b,255);

            if (phase == 1) {
                r+=2;
            }
            if (phase == 2) {
                g+=2;
            }
            if (phase == 3) {
                b+=2;
            }
            if (phase == 4) {
                r-=2;
            }
            if (phase == 5) {
                g-=2;
            }
            if (phase == 6) {
                b-=2;
            }

            if (phase == 1 && r == 255) {
                phase++;
            }
            if (phase == 2 && g == 255) {
                phase++;
            }            
            if (phase == 3 && b == 255) {
                phase++;
            }
            if (phase == 4 && r == 1) {
                phase++;
            }            
            if (phase == 5 && g == 1) {
                phase++;
            }
            if (phase == 6 && b == 1) {
                phase = 1;
            }

            hashMap.put(i, new JPanel());
            hashMap.get(i).setBackground(myColor);
            hashMap.get(i).setBounds(i, 0, 1, 100);
            myLayeredPane.add(hashMap.get(i));
        }
            
        hashMap.clear();
        phase = 1;
        r = 1;
        g = 1;
        b = 1;

        for (Integer i = 0; i < 1500; i++) {
            myColor = new Color(r,g,b,100);

            if (phase == 1) {
                r+=2;
            }
            if (phase == 2) {
                g+=2;
            }
            if (phase == 3) {
                b+=2;
            }
            if (phase == 4) {
                r-=2;
            }
            if (phase == 5) {
                g-=2;
            }
            if (phase == 6) {
                b-=2;
            }

            if (phase == 1 && r == 255) {
                phase++;
            }
            if (phase == 2 && g == 255) {
                phase++;
            }            
            if (phase == 3 && b == 255) {
                phase++;
            }
            if (phase == 4 && r == 1) {
                phase++;
            }            
            if (phase == 5 && g == 1) {
                phase++;
            }
            if (phase == 6 && b == 1) {
                phase = 1;
            }

            hashMap.put(i, new JPanel());
            hashMap.get(i).setBackground(myColor);
            hashMap.get(i).setBounds(i, 100, 1, 100);
            myLayeredPane.add(hashMap.get(i));
        }
            
        hashMap.clear();

        int c = 0;
        boolean colorChanger = false;
        for (Integer i = 0; i < 1500; i++) {
            
            myColor = new Color(c, c, c, 255);

            if (!colorChanger) {
                c++;
            }
            if (colorChanger) {
                c--;
            }
            if (c == 255) {
                colorChanger = true;
            }
            if (c == 0) {
                colorChanger = false;
            }

            hashMap.put(i, new JPanel());
            hashMap.get(i).setBackground(myColor);
            hashMap.get(i).setBounds(i, 200, 1, 100);
            myLayeredPane.add(hashMap.get(i));
        }

        c = 0;
        colorChanger = false;
        for (Integer i = 0; i < 1500; i++) {
            
            myColor = new Color(c, c, c, 100);

            if (!colorChanger) {
                c++;
            }
            if (colorChanger) {
                c--;
            }
            if (c == 255) {
                colorChanger = true;
            }
            if (c == 0) {
                colorChanger = false;
            }

            hashMap.put(i, new JPanel());
            hashMap.get(i).setBackground(myColor);
            hashMap.get(i).setBounds(i, 300, 1, 100);
            myLayeredPane.add(hashMap.get(i));
        }

        myFrame.setVisible(true);
    }
}
