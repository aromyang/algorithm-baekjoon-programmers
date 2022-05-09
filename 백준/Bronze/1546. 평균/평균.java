import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();

        double[] scoreArr = new double[testcase];
        double max = 0;

        for(int i=0; i<testcase; i++){
            int score = sc.nextInt();
            scoreArr[i] = score;
            if(scoreArr[i]>max) max = scoreArr[i];
        }

        double sum = 0;

        for(int i=0; i<scoreArr.length; i++){
            if(scoreArr[i]==max) scoreArr[i]=100;
            else scoreArr[i]= (double)(scoreArr[i]/max) *100;
            sum += scoreArr[i];

        }
        System.out.println(sum/testcase);
    }
}
