class Solution {
    public int solution(int order) {
        int answer = 0;
        while (order > 0) {
            switch (order % 10) {
                case 3:
                case 6:
                case 9:
                    answer++;
                    break;
            }
            order /= 10;
        }
        return answer;
    }
}