import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer[]> list = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            list.add(new Integer[]{Integer.parseInt(br.readLine()), i});
        }

        list.sort(Comparator.comparingInt(o -> o[0]));

        int max = 0;

        //list에 저장된 배열의 인덱스 값과 현재 리스트 인덱스 값을 비교
        for (int i = 0; i < N; i++) {
            max = Math.max(max, list.get(i)[1] - i);
        }

        System.out.println(max + 1);

    }
}
