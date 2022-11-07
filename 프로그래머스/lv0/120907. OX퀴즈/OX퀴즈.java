class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];

        for (int i = 0; i < quiz.length; i++) {
            String[] split = quiz[i].split(" ");
            switch (split[1]) {
                case "+" :
                    answer[i] = Integer.parseInt(split[0]) + Integer.parseInt(split[2]) == Integer.parseInt(split[4]) ? "O" : "X"; 
                    break;
                case "-" :
                    answer[i] = Integer.parseInt(split[0]) - Integer.parseInt(split[2]) == Integer.parseInt(split[4]) ? "O" : "X";
                    break;
            }
        }

        return answer;
    }
}