import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int computers = Integer.parseInt(br.readLine());
        int connected = Integer.parseInt(br.readLine());

        int[][] net = new int[computers][computers];
        boolean[] visited = new boolean[computers];

        for (int i = 0; i < connected; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken()) - 1;
            int to = Integer.parseInt(st.nextToken()) - 1;
            net[from][to] = 1;
            net[to][from] = 1;
        }
        
        Queue<Integer> q = new LinkedList<>();
        q.add(0);

        int answer = 0;

        while (!q.isEmpty()) {
            Integer now = q.poll();
            visited[now] = true;

            for (int i = 0; i < net[now].length; i++) {
                if (net[now][i] == 1 && !visited[i] && !q.contains(i)) {
                    answer++;
                    q.add(i);
                }
            }
        }

        System.out.println(answer);
    }

}
