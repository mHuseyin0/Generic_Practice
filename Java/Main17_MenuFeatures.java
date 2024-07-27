import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;

import javax.swing.ImageIcon;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JProgressBar;
import javax.swing.JSlider;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class Main17_MenuFeatures {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();

        JMenuBar myMenuBar = new JMenuBar();
        
        JMenu fileMenu = new JMenu("File");
        JMenu editMenu = new JMenu("Edit");
        JMenu helpMenu = new JMenu("Help");

        JMenuItem newFile = new JMenuItem("New File");
        JMenuItem openFile = new JMenuItem("Open File");
        JMenuItem saveFile = new JMenuItem("Save File");

        JMenuItem undo = new JMenuItem("Undo");
        JMenuItem copy = new JMenuItem("Copy");
        JMenuItem find = new JMenuItem("Find");

        JMenuItem showCommands = new JMenuItem("Show All Commands");
        JMenuItem about = new JMenuItem("About");

        myMenuBar.add(fileMenu);
        myMenuBar.add(editMenu);
        myMenuBar.add(helpMenu);

        fileMenu.add(newFile);
        fileMenu.add(saveFile);
        fileMenu.add(openFile);

        editMenu.add(undo);
        editMenu.add(copy);
        editMenu.add(find);

        helpMenu.add(showCommands);
        helpMenu.add(about);

        newFile.addActionListener(new ActionListener() {
            public void actionPerformed (ActionEvent e) {
                if (e.getSource() == newFile) {
                    JFrame newFrame = new JFrame();
                    newFrame.setVisible(true);
                    newFrame.setSize(300,300);
                }
            }
        });

        saveFile.addActionListener(new ActionListener() {
            public void actionPerformed (ActionEvent e) {
                if (e.getSource() == saveFile) {
                    myFrame.dispose();
                }
            }
        });

        ImageIcon myIcon1 = new ImageIcon("Icon2.jpg");
        ImageIcon myIcon2 = new ImageIcon("Icon3.jpg");

        fileMenu.setMnemonic(KeyEvent.VK_F); //Press Alt + F 

        saveFile.setMnemonic(KeyEvent.VK_S); //This works after opening the menu.
        saveFile.setIcon(myIcon1);
        helpMenu.setIcon(myIcon2);

        myFrame.setJMenuBar(myMenuBar);

        JProgressBar myProgressBar = new JProgressBar(JProgressBar.HORIZONTAL, 0, 100);

        myProgressBar.setStringPainted(true);
        myProgressBar.setValue(50);
        myProgressBar.setBackground(Color.GREEN);
        myProgressBar.setForeground(Color.black);

        if (myProgressBar.getValue() == 100) {
            myProgressBar.setString("Done!");
        }
        
        JComboBox<String> myComboBox = new JComboBox<>(new String[]{"Dog","Cat","Bird","Horse"});

        System.out.println(myComboBox.getItemCount());
        myComboBox.setEditable(true);
        myComboBox.addItem("Donkey");
        myComboBox.insertItemAt("Fish", 0);
        myComboBox.setSelectedIndex(3);
        myComboBox.setSelectedItem("Bird");
        myComboBox.removeItem("Dog");
        myComboBox.removeItemAt(1);
        //myComboBox.removeAllItems();

        JSlider mySlider = new JSlider(JSlider.VERTICAL, 0, 100, 25);
        JLabel myLabel = new JLabel("°C " + mySlider.getValue());
        myLabel.setForeground(Color.black);
        myLabel.setBackground(Color.cyan);
        myLabel.setHorizontalAlignment(JLabel.CENTER);;
        myLabel.setOpaque(true);
        mySlider.setBackground(Color.cyan);
        mySlider.setPaintTicks(true);
        mySlider.setMinorTickSpacing(5);
        mySlider.setMajorTickSpacing(10);
        mySlider.setPaintLabels(true);
        mySlider.addChangeListener(new ChangeListener() {
            public void stateChanged(ChangeEvent e) {
                if (e.getSource() == mySlider) {
                    myLabel.setText("°C " + mySlider.getValue());
                }
            }
        });
        
        JLabel mylabel2 = new JLabel();

        myFrame.setLayout(null);
        myFrame.add(mySlider);
        myFrame.add(myLabel);
        myFrame.add(myComboBox);
        myFrame.add(mylabel2);
        myFrame.add(myProgressBar);

        mySlider.setBounds(20, 20, 80, 400);
        myLabel.setBounds(20, 420, 50, 20);
        myComboBox.setBounds(20, 445, 80, 20);
        myProgressBar.setBounds(120, 20, 200, 20);
        mylabel2.setBounds(20, 420, 80, 20);
        mylabel2.setBackground(Color.cyan);
        mylabel2.setOpaque(true);

        myFrame.getContentPane().setBackground(Color.black);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setResizable(true);
        myFrame.setSize(500, 600);
        myFrame.setVisible(true);
    }
}
