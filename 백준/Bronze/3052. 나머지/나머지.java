import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] restArr = new int[10];

        for(int i=0; i<10; i++){
            int num = sc.nextInt();
            restArr[i] = (num%42);
        }
        Arrays.sort(restArr);
        int count = 1;
        int index = 0;

        for(int i=0; i<restArr.length-1; i++){
            if(restArr[i] != restArr[i+1]){
                 count++;
            }
        }

        System.out.println(count);


    }
}
