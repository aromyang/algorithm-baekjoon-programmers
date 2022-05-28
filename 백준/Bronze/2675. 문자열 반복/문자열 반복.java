import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(reader.readLine());
        
        for(int i=0; i<t; i++){
            StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
            int r = Integer.parseInt(st.nextToken());
            String s = st.nextToken();
            for(int j=0; j<s.length(); j++) {
                if (s.charAt(j) == '\\') System.out.print("\\".repeat(r));
                else System.out.print(String.valueOf(s.charAt(j)).repeat(r));
            }
            System.out.println();
        }
    }
}
