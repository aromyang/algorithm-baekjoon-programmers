import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();
        double[] ratio = new double[testcase];

        for (int i = 0; i < testcase; i++) {
            int stuNum = sc.nextInt();
            int[] arr = new int[stuNum];

            int sum = 0;
            int count = 0;
            double avg = 0;

            for(int j=0; j<arr.length; j++){
                arr[j] = sc.nextInt();
                sum+=arr[j];
            }

            avg = (sum/stuNum);

            for(int k=0; k<arr.length; k++){
                if(arr[k]>avg) count++;
            }
            ratio[i] = (double)count/stuNum*100;
        }
        for(int i=0; i<ratio.length; i++){
            System.out.printf("%.3f%%\n", ratio[i]);
        }
    }
}
