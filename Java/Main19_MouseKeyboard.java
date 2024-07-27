import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class Main19_MouseKeyboard {
    public static boolean direction = true;
    public static int a = 0;
    public static int b = 0;
    public static int c = 0;
    public static void main(String[] args) {

        //Color myColor = new JColorChooser().showDialog(null, "Color Chooser", Color.black, true);
        //System.out.println(myColor);

        JFrame myFrame = new JFrame();
        myFrame.getContentPane().setBackground(Color.black);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setResizable(true);
        myFrame.setSize(500, 400);
        
        JLabel myLabel = new JLabel();
        myLabel.setPreferredSize(new Dimension(200,200));
        myLabel.setBackground(Color.CYAN);
        myLabel.setOpaque(true);
        
        myFrame.add(myLabel);
        myFrame.setLayout(new FlowLayout(FlowLayout.LEFT));
        myFrame.pack();
        myFrame.setVisible(true);

        myFrame.addMouseWheelListener(new MouseWheelListener() {
            public void mouseWheelMoved(MouseWheelEvent e) {
                if (e.getWheelRotation() == -1) {
                    myFrame.setSize(myFrame.getWidth()+10, myFrame.getHeight());
                }
                if (e.getWheelRotation() == 1) {
                    myFrame.setSize(myFrame.getWidth()-10, myFrame.getHeight());
                }
            }
        });

        myFrame.addMouseMotionListener(new MouseMotionListener() {
            public void mouseDragged(MouseEvent e) {
                System.out.println("Mouse location: "+e.getX() +", "+ e.getY());
                try{
                    Thread.sleep(1000);            
                } catch (Exception h) {
                }
            }    
            public void mouseMoved(MouseEvent e) {
                if (direction) {
                    myLabel.setLocation(myLabel.getX()+1, myLabel.getY());
                }
                if (!direction) {
                    myLabel.setLocation(myLabel.getX()-1, myLabel.getY());
                }
                if (myLabel.getX() == 1365) {
                    direction = false;
                }
                if (myLabel.getX() == 0) {
                    direction = true;
                }
            }
        });

        myLabel.addMouseListener(new MouseListener() {
            public void mouseClicked(MouseEvent e) {
                System.out.println("You clicked the mouse.");
                System.out.println(a + " times clicked.");
                System.out.println();
                a++;
            }
            public void mousePressed(MouseEvent e) {
                System.out.println("You pressed the mouse.");
                System.out.println(b + " times pressed.");
                System.out.println();
                b++;
            }
            public void mouseReleased(MouseEvent e) {
                System.out.println("You released the mouse.");
                System.out.println(c + " times released.");
                System.out.println();
                c++;
            }
            public void mouseEntered(MouseEvent e) {
                System.out.println("You entered the label.");
            }
            public void mouseExited(MouseEvent e) {
                System.out.println("You exited the label.");
            }
        });



        myFrame.addKeyListener(new KeyListener() {
            public void keyReleased(KeyEvent e) {
            }
            public void keyPressed(KeyEvent e) {
                switch(e.getKeyCode()) {
                    case 40 : myLabel.setLocation(myLabel.getX(), myLabel.getY()+50);
                    break;
                    case 38 : myLabel.setLocation(myLabel.getX(), myLabel.getY()-50);
                    break;
                    case 37 : myLabel.setLocation(myLabel.getX()-50, myLabel.getY());
                    break;
                    case 39 : myLabel.setLocation(myLabel.getX()+50, myLabel.getY());
                    break;
                }
                
            }
            public void keyTyped(KeyEvent e) {
                switch(e.getKeyChar()) {
                    case 's' : myLabel.setLocation(myLabel.getX(), myLabel.getY()+5);
                    break;
                    case 'w' : myLabel.setLocation(myLabel.getX(), myLabel.getY()-5);
                    break;
                    case 'a' : myLabel.setLocation(myLabel.getX()-5, myLabel.getY());
                    break;
                    case 'd' : myLabel.setLocation(myLabel.getX()+5, myLabel.getY());
                    break;
                }
            }
        });
    }
}
