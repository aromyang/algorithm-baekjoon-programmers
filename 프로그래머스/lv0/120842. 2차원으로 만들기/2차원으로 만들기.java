class Solution {
    public int[][] solution(int[] num_list, int n) {
        int[][] answer = new int[num_list.length / n][n];
        int start = 0;
        for (int i = 0; i < num_list.length; i+=n) {
            System.arraycopy(num_list, i, answer[start], 0, n);
            start++;
        }
        return answer;
    }
}