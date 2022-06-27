import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int count = 1;
        int start = 1;
        int end = 1;
        int sum = 1;

        while(end != N) {
            if(sum < N) {
                end++;
                sum += end;
            }
            else if(sum > N) {
                sum -= start;
                start++;
            }
            else {
                count++;
                end++;
                sum += end;
            }
        }
        System.out.println(count);
    }
}
