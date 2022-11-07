class Solution {
    public int solution(int chicken) {
        int answer = 0;
        int left = 0;

        while (chicken >= 10) {
            left = chicken % 10;
            answer += (chicken /= 10);
            chicken += left;
        }
        
        return answer;
    }
}