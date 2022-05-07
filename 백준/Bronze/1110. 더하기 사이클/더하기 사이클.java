import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int temp = num;
        int cycle = 0;

        while(true){
            temp = (temp/10 + temp%10)%10 + (temp%10)*10;
            cycle++;
            if(temp == num) break;
        }
        System.out.println(cycle);
    }
}
