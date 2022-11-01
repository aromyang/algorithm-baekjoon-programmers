class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for (int a = i; a <= j; a++) {
            int now = a;
            while (now > 0) {
                if (now % 10 == k) {
                    answer++;
                }
                now /= 10;
            }
        }
        return answer;
    }
}