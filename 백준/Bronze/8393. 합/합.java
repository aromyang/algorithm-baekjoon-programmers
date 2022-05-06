import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        int n = sc.nextInt();
        for(int i=0; i<=n; i++){
            sum += i;
        }
        System.out.println(sum);
    }
}