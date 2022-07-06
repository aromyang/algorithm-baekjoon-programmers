import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] arr = new long[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        int count = 0;

        for(int i=0; i<N; i++) {
            long target = arr[i];
            int start = 0;
            int end = N-1;

            while(start < end) {
                if(arr[start] + arr[end] == target) {
                    if (start != i && end != i) {
                        count++;
                        break;
                    } else if (start == i) {
                        start++;
                    } else if (end == i) {
                        end--;
                    }
                } else if (arr[start] + arr[end] < target) {
                    start++;
                } else {
                    end--;
                }
            }
        }

        System.out.println(count);

    }
}
