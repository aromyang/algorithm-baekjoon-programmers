import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 버블 정렬 이용하기
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int[] numbers = new int[input.length()];

        for (int i = 0; i < input.length(); i++) {
            numbers[i] = input.charAt(i) - '0';
        }

        for (int i = 0; i < input.length(); i++) {
            int max = i;
            for (int j = i + 1; j < input.length(); j++) {
                if (numbers[j] > numbers[max]) {
                    max = j;
                }
                if (numbers[i] < numbers[max]) {
                    int temp = numbers[i];
                    numbers[i] = numbers[max];
                    numbers[max] = temp;
                }
            }
        }

        for (int i = 0; i < input.length(); i++) {
            System.out.print(numbers[i]);
        }

    }

}
