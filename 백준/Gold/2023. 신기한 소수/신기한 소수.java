import java.io.*;

public class Main {
    static BufferedWriter bw;
    static int target;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        target = Integer.parseInt(br.readLine());
        dfs(2, 1);
        dfs(3, 1);
        dfs(5, 1);
        dfs(7, 1);
        bw.close();
    }

    static void dfs(int number, int depth) throws IOException {
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        if (depth == target) {
            if (isPrime(number)) {
                bw.write(number + "\n");
                bw.flush();
            }
            return;
        }

        for (int i = 1; i < 10; i++) {
            if (i % 2 == 0) {
                continue;
            }
            if (isPrime(number * 10 + i)) {
                dfs(number * 10 + i, depth + 1);
            }
        }

    }
    static boolean isPrime(int n) {
        if (n == 1) {
            return false;
        }
        for (int i = 3; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
