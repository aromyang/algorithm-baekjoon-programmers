import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        Queue<Integer> cards = new LinkedList<>();
        for(int i=1; i<=n; i++){
            cards.add(i);
        }

        while(cards.size()!=1){
            cards.poll();
            cards.add(cards.poll());
        }
        System.out.println(cards.poll());
    }
}