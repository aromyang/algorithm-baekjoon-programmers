class Solution {
    public int solution(int n, int t) {
        int answer = n;
        while (t != 0) {
            t--;
            answer *= 2;
        }
        return answer;
    }
}