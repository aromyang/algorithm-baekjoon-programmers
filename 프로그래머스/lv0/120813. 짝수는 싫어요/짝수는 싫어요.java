class Solution {
    public int[] solution(int n) {
        int[] answer;
        if (n % 2 == 0) {
            answer = new int[n / 2];
        } else {
            answer = new int[(n / 2) + 1];
        }

        answer[0] = 1;
        if (answer.length == 1) return answer;
        
        for (int i = 1; i < answer.length; i ++) {
            answer[i] += answer[i-1] + 2;
        }
        
        return answer;
    }
}