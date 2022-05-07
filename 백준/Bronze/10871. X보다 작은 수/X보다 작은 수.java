import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");

        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        StringBuilder builder = new StringBuilder();

        st = new StringTokenizer(reader.readLine(), " ");

        for(int i=0; i<n; i++){
            int value = Integer.parseInt(st.nextToken());
            if(value<x){
                builder.append(value).append(' ');
            }
        }
        System.out.println(builder);
    }
}
