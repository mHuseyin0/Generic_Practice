import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.border.Border;

public class Main14_JTextField {
    public static void main(String[] args) {
        JFrame myFrame = new JFrame();

        Border myBorder = BorderFactory.createLineBorder(Color.darkGray, 5, true);

        JTextField myTextField = new JTextField();
        myTextField.setBackground(Color.gray);
        myTextField.setForeground(Color.black);
        myTextField.setCaretColor(Color.black);
        myTextField.setBorder(myBorder);
        myTextField.setText("Hello");
        myTextField.setEditable(false);
        myTextField.setSelectionStart(1);
        myTextField.setSelectionEnd(4);
        myTextField.setSelectionColor(Color.cyan);
        myTextField.setSelectedTextColor(new Color(230, 60, 60, 255));
        myTextField.setToolTipText("Please enter a text.");
        myTextField.setPreferredSize(new Dimension(250,60));
        myTextField.setFont(new Font("Times New Roman", Font.ITALIC | Font.BOLD, 30));

        JButton myButton = new JButton("Enter");
        myButton.setSize(60, 40);
        myButton.setBackground(new Color(0, 255, 255, 200));
        myButton.setForeground(Color.black);
        myButton.setFocusable(false);

        myFrame.add(myButton);
        myFrame.add(myTextField);
        myFrame.getContentPane().setBackground(Color.black);
        myFrame.setLayout(new FlowLayout(FlowLayout.LEADING));
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.pack();
        myFrame.setResizable(false);
        myFrame.setVisible(true);

        myButton.addActionListener(new ActionListener() {
            public void actionPerformed (ActionEvent e) {
                if (e.getSource() == myButton){
                    System.out.println(myTextField.getText());
                    myFrame.dispose();
                }    
            }
        });
    }
}
