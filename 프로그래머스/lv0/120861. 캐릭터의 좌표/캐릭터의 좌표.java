class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int row = board[0] / 2;
        int col = board[1] / 2;

        int[] answer = new int[2];

        for (String k : keyinput) {
            if (answer[0] < row && k.equals("right")) {
                answer[0]++;
            } else if (answer[0] > -row && k.equals("left")) {
                answer[0]--;
            } else if (answer[1] < col && k.equals("up")) {
                answer[1]++;
            } else if (answer[1] > -col && k.equals("down")) {
                answer[1]--;
            }
        }
        return answer;
    }
}