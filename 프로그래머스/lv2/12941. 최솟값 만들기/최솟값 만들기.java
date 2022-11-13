import java.util.Arrays;

class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int answer = 0;

        for (int i = 0; i < A.length; i++) {
            int j = A.length - i - 1;
            answer += A[i] * B[j];
        }

        return answer;
    }
}