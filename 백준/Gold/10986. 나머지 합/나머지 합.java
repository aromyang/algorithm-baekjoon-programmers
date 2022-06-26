import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long[] remainder = new long[M];

        long count = 0;
        long sum = 0;

        st = new StringTokenizer(br.readLine());

        for(int i=0; i<N; i++) {
            sum += Long.parseLong(st.nextToken());
            remainder[(int)(sum % M)]++;
        }

        count += remainder[0];

        for(int i=0; i<M; i++) {
            count += (remainder[i] * (remainder[i]-1)) / 2;
        }

        System.out.println(count);
    }
}
