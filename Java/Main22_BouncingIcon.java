import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

class MyPanel1 extends JPanel implements ActionListener{

    public int panelWidth = 500;
    public int panelHeight = 500;
    
    Image myImage = new ImageIcon("Icon3.jpg").getImage();

    public int locX = (int) (Math.random()*(panelWidth-myImage.getWidth(null)));
    public int locY = (int) (Math.random()*(panelHeight-myImage.getHeight(null)));

    int xVelocity = 3;
    int yVelocity = 2;

    MyPanel1() {
        this.setPreferredSize(new Dimension(500, 500));
        this.setBackground(Color.BLACK);
        
        if (Math.random() < .5) {
            xVelocity = xVelocity * -1;
        }
        if (Math.random() < .5) {
            yVelocity = yVelocity * -1;
        }

        Timer myTimer = new Timer(10, this);
        myTimer.start();

    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2D = (Graphics2D) g;

        g2D.drawImage(myImage, locX, locY, null);
    }

    public void actionPerformed(ActionEvent e) {

        if (locX > panelWidth-myImage.getWidth(null) || locX < 0) {
            xVelocity = xVelocity * -1;
        }
        
        if (locY > panelWidth-myImage.getHeight(null) || locY < 0) {
            yVelocity = yVelocity * -1;
        }

        locX = locX + xVelocity;
        locY = locY + yVelocity;
        repaint();
    }
}
public class Main22_BouncingIcon {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();
        myFrame.getContentPane().setBackground(Color.yellow);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setLayout(new FlowLayout(FlowLayout.CENTER,0,0));
        
        myFrame.setVisible(true);
        MyPanel1 myPanel = new MyPanel1();      
        
        myFrame.add(myPanel);
        myFrame.pack();
        myFrame.setLocationRelativeTo(null);
    }
}
