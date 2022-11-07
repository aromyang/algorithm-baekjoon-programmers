class Solution {
    public String solution(String polynomial) {
        String[] split = polynomial.split(" ");
        int x = 0;
        int num = 0;
        for (String s : split) {
            if (s.equals("+")) {
                continue;
            }

            if (s.contains("x")) {
                if (s.length() == 1) {
                    x += 1;
                } else {
                    x += Integer.parseInt(s.substring(0, s.length() - 1));
                }
            } else {
                num += Integer.parseInt(s);
            }
        }
        String answer = "";
        if (x != 0) {
            if (x == 1) {
                answer += "x";
            } else {
                answer += x + "x";
            }

            if (num == 0) {
                return answer;
            } else {
                answer += " + " + num;
            }
        } else {
            answer += num;
        }

        return answer;
    }
}