import java.util.Random;

public class Main3_Math {
        public static void main(String[] args) {
            
            double pi=3.14;
            double e=2.718;

            System.out.println(Math.abs(e));
            System.out.println(Math.max(e,pi));
            System.out.println(Math.round(e));
            System.out.println(Math.floor(e));
            System.out.println(Math.ceil(pi));
                
            Random myRandom=new Random();
            int x= myRandom.nextInt(6);//Random variable between 0 and 5.
            double y=myRandom.nextDouble(-50, 100);
            boolean z=myRandom.nextBoolean();
            System.out.println(x+"  "+y+"  "+z);

        }
}
