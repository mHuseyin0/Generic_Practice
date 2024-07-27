import java.awt.Color;
import java.awt.BasicStroke;
import java.awt.FlowLayout;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;

import javax.swing.JFrame;
import javax.swing.ImageIcon;
import javax.swing.JPanel;

class MyPanel extends JPanel {

    public static Image img = new ImageIcon("Icon2.jpg").getImage();
    
    public MyPanel() {
        this.setPreferredSize(new Dimension(500, 500));
    }
    
    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2D = (Graphics2D) g;
        
        //g2D.setBackground(Color.BLACK);

        g2D.setPaint(Color.blue);
        g2D.setStroke(new BasicStroke(5));
        g2D.drawLine(0, 0, 500, 500);
        
        g2D.setPaint(Color.GRAY);
        g2D.fillRect(200, 200, 100, 100);
        g2D.draw3DRect(100, 100, 300, 300, true);
        g2D.fill3DRect(225, 225, 50, 50, true);
        
        g2D.setPaint(Color.yellow);
        g2D.drawOval(395, 395, 100, 100);
        g2D.fillOval(240, 240, 20, 20);

        g2D.drawArc(5, 5, 100, 100, 225, -180);
        g2D.setPaint(Color.cyan);
        g2D.fillArc(5, 5, 100, 100, 225, 180);

        g2D.drawPolygon(new int[] {0,500,0},new int[] {0,0,500}, 3);
        g2D.setPaint(Color.red);
        g2D.setFont(new Font("Calibri", Font.BOLD, 25));
        g2D.drawString("Kind of good paint, isn't it?", 115, 50);

        g2D.drawImage(img, 400, 34, null);

    }
}

public class Main21_GraphicsBasics{
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setLayout(new FlowLayout(FlowLayout.CENTER,0,0));
        MyPanel myPanel = new MyPanel();
        myPanel.setBackground(Color.black);

        myFrame.add(myPanel);
        myFrame.pack();
        myFrame.setLocationRelativeTo(null);
        myFrame.setVisible(true);
    }

}
