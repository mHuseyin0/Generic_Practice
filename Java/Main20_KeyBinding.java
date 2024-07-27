import java.awt.Color;
import java.awt.event.ActionEvent;

import javax.swing.AbstractAction;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.KeyStroke;

public class Main20_KeyBinding {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setSize(420, 420);
        myFrame.setLayout(null);
        // If a JFrame wanted to has a keybinding:
        //myFrame.getRootPane().getInputMap(JComponent.WHEN_IN_FOCUSED_WINDOW/*not neccessary*/).put(null, myFrame);
        //myFrame.getRootPane().getActionMap().put(myFrame, null);

        JLabel myLabel = new JLabel();
        myLabel.setBounds(0, 0, 100, 100);
        myLabel.setBackground(Color.GRAY);
        myLabel.setOpaque(true);

        myLabel.getInputMap().put(KeyStroke.getKeyStroke('w'), "up");
        myLabel.getActionMap().put("up", new AbstractAction() {
            public void actionPerformed(ActionEvent e) {
                myLabel.setLocation(myLabel.getX(), myLabel.getY()-5);
            }
        });

        myLabel.getInputMap().put(KeyStroke.getKeyStroke('s'), "down");
        myLabel.getActionMap().put("down", new AbstractAction() {
            public void actionPerformed(ActionEvent e) {
                myLabel.setLocation(myLabel.getX(), myLabel.getY()+5);
            }
        });

        myLabel.getInputMap().put(KeyStroke.getKeyStroke('a'), "left");
        myLabel.getActionMap().put("left", new AbstractAction() {
            public void actionPerformed(ActionEvent e) {
                myLabel.setLocation(myLabel.getX()-5, myLabel.getY());
            }
        });

        myLabel.getInputMap().put(KeyStroke.getKeyStroke('d'), "right");
        myLabel.getActionMap().put("right", new AbstractAction() {
            public void actionPerformed(ActionEvent e) {
                myLabel.setLocation(myLabel.getX()+5, myLabel.getY());
            }
        });

        myFrame.add(myLabel);
        myFrame.setVisible(true);
    }
}
