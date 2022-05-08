import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        String str = Integer.toString(a*b*c);
        int[] count = new int[10];

        for(int i=0; i<str.length(); i++){
            for(int j=0; j<10; j++){
                if( str.charAt(i) == Character.forDigit(j, 10) ) count[j]++;
            }
        }
        for(int i=0; i<10; i++){
            System.out.println(count[i]);
        }
    }
}
