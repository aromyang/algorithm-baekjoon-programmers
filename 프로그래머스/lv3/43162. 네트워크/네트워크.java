import java.util.*;

class Solution {
    static boolean[] visited;

    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                bfs(computers, i);
            }
        }
        
        return answer;
    }
    
    public static void bfs(int[][] computers, int vertex) {
        Queue<Integer> q = new LinkedList<>();
        q.add(vertex);

        while (!q.isEmpty()) {
            Integer now = q.poll();
            visited[now] = true;

            for (int i = 0; i < computers[now].length; i++) {
                if (computers[now][i] == 1 && !visited[i] && !q.contains(i)) {
                    q.add(i);
                }
            }
        }
    }

}