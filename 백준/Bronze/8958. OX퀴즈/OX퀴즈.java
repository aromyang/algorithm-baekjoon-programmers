import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();
        String[] quiz = new String[testcase];


        for (int i = 0; i < testcase; i++) {
            quiz[i] = sc.next();
        }

        for(int i=0; i<quiz.length; i++){
            int score = 0;
            int scoreSum = 0;
            for (int j = 0; j < quiz[i].length(); j++) {
                if (quiz[i].charAt(j) == 'O') score++;
                else score = 0;
                scoreSum += score;
            }
            System.out.println(scoreSum);
        }
    }
}