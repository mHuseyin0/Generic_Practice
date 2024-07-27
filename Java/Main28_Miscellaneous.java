import java.awt.AWTException;
import java.awt.HeadlessException;
import java.awt.KeyEventDispatcher;
import java.awt.KeyboardFocusManager;
import java.awt.MouseInfo;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.awt.event.KeyEvent;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Hashtable;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Stack;

public class Main28_Miscellaneous {
    public static void main(String[] args) throws AWTException, InterruptedException, HeadlessException, UnsupportedFlavorException, IOException {
        Stack<String> stack = new Stack<>();  //LIFO
        stack.push("First element");
        stack.push("Second element");
        stack.push("Third element");
        stack.push("Fourth element");

        String lastElement = stack.pop();
        System.out.println(lastElement);
        System.out.println(stack.peek());
        System.out.println(stack);
        System.out.println(stack.search("First element"));
        System.out.println(stack.search("Abstract element"));

        System.out.println();
        System.out.println();

        Queue<String> queue = new LinkedList<>(); //FIFO
        queue.offer("First one");
        queue.offer("Second one");
        queue.offer("Third one");
        System.out.println(queue);
        queue.poll();
        System.out.println(queue.peek());
        System.out.println(queue);
        //Unlike add(),remove(), and element(); offer(), poll(), and peek() methods don't throw exception.
        System.out.println(queue.isEmpty());
        System.out.println(queue.size());
        System.out.println(queue.contains("Second one"));

        Queue<Double> myQueue = new PriorityQueue<>(Collections.reverseOrder());
        myQueue.offer(3.0);
        myQueue.offer(5.0);
        myQueue.offer(1.0);
        myQueue.offer(4.0);
        myQueue.offer(2.0);

        while (!myQueue.isEmpty()) {
            System.out.println(myQueue.poll());
        }

        LinkedList<String> linkedList = new LinkedList<>();

        linkedList.push("A");
        linkedList.push("B");
        linkedList.push("C");
        linkedList.push("D");
        System.out.println(linkedList);
        linkedList.pop();
        System.out.println(linkedList);
        linkedList.poll();
        System.out.println(linkedList);
        linkedList.offer("F");   //To add an element to the tail of the linked list like a queue
        linkedList.add("G");     //To add an element to the tail of the linked list like a queue
        linkedList.add(0, "H");
        System.out.println(linkedList);
        System.out.println(linkedList.indexOf("B"));
        System.out.println(linkedList.peekFirst());
        System.out.println(linkedList.peek());
        System.out.println(linkedList.peekLast());
        System.out.println(linkedList);

        int[] arrayList = new int[1000000];
        
        for (int i = 0; i < 1000000; i++) {
            arrayList[i] = i;
        }
        System.out.println(Arrays.binarySearch(arrayList, 0, arrayList.length, 232323));  
        //This will eliminate the half of the list everytime.(List must be sorted to use binary search.)
        //(Good at very large data sets.)

        move(10);
        System.out.println(factorial(5));

        Hashtable<Integer, String> table = new Hashtable<>();

        table.put(100, "Student 1");
        table.put(101, "Student 2");
        table.put(102, "Student 3");
        table.put(103, "Student 4");
        table.put(104, "Student 5");

        table.remove(102);

        for (Integer i : table.keySet()) {
            System.out.println(i.hashCode() + "\t" + i + "\t:" + table.get(i));
        }

        Robot myRobot = new Robot();

        myRobot.keyPress(KeyEvent.VK_ALT);
        myRobot.keyPress(KeyEvent.VK_TAB);
        myRobot.keyRelease(KeyEvent.VK_TAB);
        myRobot.keyRelease(KeyEvent.VK_ALT);

        KeyboardFocusManager.getCurrentKeyboardFocusManager()
        .addKeyEventDispatcher(new KeyEventDispatcher() {
            @Override
            public boolean dispatchKeyEvent(KeyEvent e) {
              System.out.println("Got key event!");
              return false;
            }
        });
        KeyboardFocusManager.getCurrentKeyboardFocusManager().getActiveWindow(); 
        KeyboardFocusManager.getCurrentKeyboardFocusManager().getFocusedWindow();
        //Both returns null???
        

        /*while (true) {
            System.out.print("");
        }*/

        System.out.println(MouseInfo.getPointerInfo().getLocation());

        long start = System.nanoTime();
        Thread.sleep(3000);
        long duration = (System.nanoTime()-start);///1000000 to get miliseconds
        System.out.println("Duration = "+ duration + " ns.");
        
        System.out.println(Toolkit.getDefaultToolkit().getSystemClipboard().getData(DataFlavor.stringFlavor));
        //How to use Clipboard class?

        /*File file = new File("");
        file.getAbsoluteFile();
        file.mkdirs();*/
    }

    private static int factorial(int i) {
        if (i == 0) return 1;
        return i * factorial(i-1);
    }

    private static void move(int i) {
        if (i < 1) {
            System.out.println("You arrived!");
            return;
        }
        
        else {
            System.out.println("Remaining steps to arrive: "+ i);
            move(i-1);
        }
    }
}
