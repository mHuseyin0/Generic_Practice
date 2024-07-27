class myThread extends Thread {
    @Override
    public void run() {
        for (int i = 1; i <= 10; i++) {
            System.out.println("Thread 2: "+ i);
            System.out.println();
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

class myRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable task is working.");
    }
}

public class Main27_Threads {
    public static void main(String[] args) throws InterruptedException {
        //System.out.println(Thread.activeCount());
        //Thread.currentThread().setName("Main27");
        //System.out.println(Thread.currentThread().getName());
        //The higher number, the higher priority for this thread.
        //Thread.currentThread().setPriority(1);
        //System.out.println(Thread.currentThread().getPriority());
        //System.out.println(Thread.currentThread().isAlive());
        myThread thread2 = new myThread();
        thread2.setDaemon(true);
        thread2.start();
        Thread.currentThread().setPriority(10);
        //Thread priority is between 1 and 10.
        for (int i = 1; i <= 3; i++) {
            System.out.println("Thread 1: "+ i);
            System.out.println();
            Thread.sleep(1000);
        }
        //JVM terminates itself when all user threads (non-daemon threads) finish their execution.
        //Daemon thread is a low priority thread that runs in background to perform tasks.

        //System.out.println(thread2.getName());
        //thread2.setName("myThread1");
        //System.out.println(thread2.getPriority());
        //System.out.println(thread2.isDaemon());

        //Second way of creating a thread (via Runnable interface)
        //This can be more useful because it is possible to inherit another class
        
        myRunnable runnable1 = new myRunnable();
        Thread thread3 = new Thread(runnable1);
        thread2.join();
        //Main thread will wait until thread2 is finished.
        thread3.start();

        //Even if a thread throws an exception, the other ones will continue execution.
    }
}
