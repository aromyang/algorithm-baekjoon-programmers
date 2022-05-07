import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

            int testcase = Integer.parseInt(reader.readLine());

            for(int i=0; i<testcase; i++){
                StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
                writer.write((Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken())+"\n"));
            }
            writer.flush();
            writer.close();

    }
}
