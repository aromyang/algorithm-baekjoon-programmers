import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0; i<n; i++){
            int num = Integer.parseInt(reader.readLine());
            list.add(num);
        }
        
        list.stream()
                .sorted()
                .forEach(i -> System.out.println(i));
    }
}
