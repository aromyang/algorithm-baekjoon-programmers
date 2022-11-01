class Solution {
    public int solution(int n) {
        String number = String.valueOf(n);
        int answer = 0;
        for (int i = 0; i < number.length(); i++) {
            answer += number.charAt(i) - '0';
        }
        return answer;
    }
}