class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        for (int i = -num; i <= total; i++) {
            int sum = 0;
            int now = i;
            
            for (int j = 0; j < num; j++) {
                sum += now++;
            }
            
            if (sum == total) {
                for (int j = 0; j < num; j++) {
                    answer[j] = i++;
                }
                return answer;
            }
        }
        
        return answer;
    }
}