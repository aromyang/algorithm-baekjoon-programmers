import java.io.*;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        Deque<Node> deque = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());

            //deque.getLast().value의 값이 now보다 크다면 제거
            //&& 반복: !deque.isEmpty()
            while (!deque.isEmpty() && deque.getLast().value > now) {
                deque.removeLast();
            }
            //-> deque에는 getLast의 value가 now보다 같거나 작은 경우만 남음


            //deque의 마지막에 now 값을 넣어주기
            deque.addLast(new Node(now, i));

            //-> 현재 deque: 삽입된 값의 last는 항상 now보다 작은 상태에서 마지막에 now 삽입
                //-> A1, A1~A2, A1~A3로 시작되었으므로 항상 first의 값이 최소값이 됨
                    //-> 정렬 완료


            //인덱스가 범위를 벗어나면 제거
            if (deque.getFirst().index <= i - L) {
                deque.removeFirst();
            }

            //최소값 출력
            bw.write(deque.getFirst().value + " ");

        }

        bw.flush();
        bw.close();

    }

    static class Node {
        int value;
        int index;

        public Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}
