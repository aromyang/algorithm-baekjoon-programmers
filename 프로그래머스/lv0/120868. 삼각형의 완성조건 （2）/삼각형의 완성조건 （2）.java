class Solution {
    public int solution(int[] sides) {
        int max, min;

        if (sides[0] >= sides[1]) {
            max = sides[0];
            min = sides[1];
        } else {
            max = sides[1];
            min = sides[0];
        }

        int answer = 0;

        int side = max;
        while (max < min + side) {
            side--;
            answer++;
        }

        side = max + 1;
        while (side < min + max) {
            side++;
            answer++;
        }

        return answer;
    }
}