import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N]; //원본 배열
        int[] sum = new int[N]; //합 배열
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        //삽입 정렬
        for (int i = 1; i < N; i++) {
            int pointer = i;
            int now = arr[i];

            for (int j = i - 1; j >= 0; j--) {
                if (arr[j] < arr[i]) {
                    pointer = j+1;
                    break;
                }
                if (j == 0) {
                    pointer = 0;
                }
            }
            for (int j = i; j > pointer; j--) {
                arr[j] = arr[j - 1];
            }
            arr[pointer] = now;
        }

        //합 배열
        sum[0] = arr[0];
        for (int i = 1; i < N; i++) {
            sum[i] = sum[i - 1] + arr[i];
        }

        //전체 합
       int result = Arrays.stream(sum).sum();

        System.out.println(result);
    }
}
