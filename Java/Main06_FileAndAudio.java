import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import javax.sound.sampled.*;

public class Main6_FileAndAudio {
    public static void main(String[] args) {
        
        try {
            FileWriter myWriter = new FileWriter("MyFile.txt");
            myWriter.write("This is written by java.");
            myWriter.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        try {
            FileReader myReader = new FileReader("MyFile.txt");
            int data = myReader.read();
            while (data != -1) {
                System.out.print((char)data);
                data = myReader.read();
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            File myFile = new File("C:\\Users\\Muhammed\\Documents\\Coding\\VisualStudio\\RAVE.wav");
            AudioInputStream myAudio = AudioSystem.getAudioInputStream(myFile);
            Clip myClip = AudioSystem.getClip();
            myClip.open(myAudio);
            myClip.start();
            myClip.loop(Clip.LOOP_CONTINUOUSLY);
       
            String choice = "";
            long clipPosition;
            int minute = 0;
            int second = 0;
            int time = 0;
            Scanner myScanner = new Scanner(System.in);
            System.out.println();
            System.out.println("CONTROL PANEL\nP: Pause\nS: Start\nB: Rewind to the beginning\nR: Rewind 5 seconds\nF: Fast forward 5 seconds\nQ: Quit\nT: Time played\nTT: Remaining time\nTTT: Total time");
            while (!choice.equals("Q")) {
            choice = myScanner.nextLine();
            choice = choice.toUpperCase();
            
            switch(choice) {
                case ("P") : myClip.stop();
                break;
                case ("S") : myClip.start();
                break;
                case ("T") :
                time = (int)(myClip.getMicrosecondPosition()/1000000);
                second = time%60;
                minute = (time-second)/60;
                System.out.printf("Time: %d:%02d ",minute,second);
                System.out.println();
                break;
                case ("TT") :
                time = (int)(myClip.getMicrosecondLength()-myClip.getMicrosecondPosition())/1000000;
                second = time%60;
                minute = (time-second)/60;
                System.out.printf("Remaining time: %d:%02d ",minute,second);
                System.out.println();
                break;
                case ("TTT") :
                time = (int)(myClip.getMicrosecondLength()/1000000);
                second = time%60;
                minute = (time-second)/60;
                System.out.printf("Total media time: %d:%02d",minute,second);
                System.out.println();
                break;
                case ("B") : myClip.setMicrosecondPosition(0);
                break;
                case ("R") : clipPosition = myClip.getMicrosecondPosition();
                myClip.setMicrosecondPosition(clipPosition- 5000000);
                break;
                case ("F") : clipPosition = myClip.getMicrosecondPosition();
                myClip.setMicrosecondPosition(clipPosition+ 5000000);
                break;
                case ("Q") : myClip.close();
                break;
                default : System.out.println("Invalid input!");
            }
        }  
        myScanner.close();
        } catch (Exception e) {
        }
          
    }
}
