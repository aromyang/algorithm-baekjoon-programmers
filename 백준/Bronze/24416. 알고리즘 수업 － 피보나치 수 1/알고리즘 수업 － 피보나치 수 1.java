import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(fibDynamic(n) + " " + (n-2));
    }
    static int fibDynamic(int n){
        int[] fib = new int[n+1];
        fib[1]=fib[2]=1;
        for(int i=3; i<=n; i++){
            fib[i] = fib[i-1] + fib[i-2];
        }
        return fib[n];
    }
}
