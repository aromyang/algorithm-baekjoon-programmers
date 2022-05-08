import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[sc.nextInt()];
        int min = 1000000, max = -1000000;

        for(int i=0; i<arr.length; i++){
            arr[i] = sc.nextInt();
            max = arr[i]>max ? arr[i] : max;
            min = arr[i]<min ? arr[i] : min;
        }
        System.out.println(min + " " + max);
    }
}
