import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] sequence = new int[N];
        for (int i = 0; i < N; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        int[] answer = new int[N];

        //인덱스를 저장하기 위한 스택 생성
        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        //스택에서 인덱스를 가져와 순회하면서 오큰 넘버를 answer에 저장
        for (int i = 1; i < N; i++) {
            while (!stack.isEmpty() && sequence[stack.peek()] < sequence[i]) {
                answer[stack.pop()] = sequence[i];
            }
            stack.push(i);
        }

        while (!stack.isEmpty()) {
            answer[stack.pop()] = -1;
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int a : answer) {
            bw.write(a + " ");
        }
        bw.flush();
        bw.close();
    }
}
