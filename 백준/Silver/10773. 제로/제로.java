import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(reader.readLine());

        Stack<Integer> correct = new Stack<>();

        for(int i=0; i<k; i++){
            int temp = Integer.parseInt(reader.readLine());

            if(temp==0) correct.pop();
            else correct.push(temp);
        }

        int result = correct.stream().mapToInt(i->i).sum();
        System.out.println(result);
    }
}