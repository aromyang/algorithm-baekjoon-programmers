class Solution {
    public int solution(int n) {
        int answer = 1;
        int pizza = 6;
        while ((answer * pizza) % n != 0) {
            answer++;
        }
        return answer;
    }
}