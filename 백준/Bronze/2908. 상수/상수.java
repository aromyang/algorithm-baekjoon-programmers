import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int reverseA = 0;
        int reverseB = 0;

        for(int i=100; i>0; i/=10){
            reverseA += (a%10)*i;
            a /= 10;
        }
        for(int i=100; i>0; i/=10) {
            reverseB += (b % 10) * i;
            b /= 10;
        }

        System.out.println(Math.max(reverseA, reverseB));

    }
}
