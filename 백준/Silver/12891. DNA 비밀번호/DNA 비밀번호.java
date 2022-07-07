import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] valid;
    static int[] password;
    static int answer;
    static int check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        char[] dna = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());

        check = 0;
        answer = 0;

        valid = new int[4];
        password = new int[4];

        
        //초기값 처리
        for (int i = 0; i < 4; i++) {
            valid[i] = Integer.parseInt(st.nextToken());
            if (valid[i] == 0) check++;
        }
        
        for (int i = 0; i < P; i++) add(dna[i]);
        if(check == 4) answer++;

        
        //하나씩 빼고 더하기
        for (int i = P; i < S; i++) {
            remove(dna[i-P]);
            add(dna[i]);

            if(check == 4) answer++;
        }

        System.out.println(answer);

    }

    private static void add(char c) {
        switch (c) {
            case 'A':
                password[0]++;
                if (password[0] == valid[0]) check++;
                break;
            case 'C':
                password[1]++;
                if (password[1] == valid[1]) check++;
                break;
            case 'G':
                password[2]++;
                if (password[2] == valid[2]) check++;
                break;
            case 'T':
                password[3]++;
                if (password[3] == valid[3]) check++;
                break;
        }
    }

    private static void remove(char c) {
        switch (c) {
            case 'A':
                if (password[0] == valid[0]) check--;
                password[0]--;
                break;
            case 'C':
                if (password[1] == valid[1]) check--;
                password[1]--;
                break;
            case 'G':
                if (password[2] == valid[2]) check--;
                password[2]--;
                break;
            case 'T':
                if (password[3] == valid[3]) check--;
                password[3]--;
                break;
        }
    }

}
