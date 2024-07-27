import java.util.Calendar;
import java.util.Timer;
import java.util.TimerTask;

public class Main26_TimerTask {
    static int numTask = 5;
    public static void main(String[] args) {
        Timer myTimer = new Timer();
        TimerTask myTask = new TimerTask() {
            @Override
            public void run() {
                System.out.println("Task is completed.");
                numTask--;
                if (numTask == 0) {
                    myTimer.cancel();
                }
            }
        };
        
        Calendar date = Calendar.getInstance();
        //System.out.println(date);
        date.set(Calendar.YEAR,2023);
        date.set(Calendar.MONTH,Calendar.AUGUST);
        date.set(Calendar.DAY_OF_MONTH,11);
        date.set(Calendar.HOUR_OF_DAY,14);
        date.set(Calendar.MINUTE,38);
        date.set(Calendar.SECOND,5);
        date.set(Calendar.MILLISECOND,500);

        //A timer must be scheduled just once.
        //myTimer.schedule(myTask, 0);
        //myTimer.schedule(myTask, date.getTime());
        myTimer.scheduleAtFixedRate(myTask, date.getTime(), 5000);
    }
}
