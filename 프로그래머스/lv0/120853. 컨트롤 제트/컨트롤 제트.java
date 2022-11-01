class Solution {
    public int solution(String s) {
        String[] strs = s.split(" ");
        int answer = !strs[0].equals("Z") ? Integer.parseInt(strs[0]) : 0;
        for (int i = 1; i < strs.length; i++) {
            if (strs[i].equals("Z")) {
                if (!strs[i - 1].equals("Z")) {
                    answer -= Integer.parseInt(strs[i - 1]);
                } else {
                    int index = i - 1;
                    while (index >= 0) {
                        if (strs[index].equals("Z")) {
                            index--;
                        } else {
                            answer -= Integer.parseInt(strs[index]);
                            break;
                        }
                        index--;
                    }
                }
            } else {
                answer += Integer.parseInt(strs[i]);
            }
        }
        return answer;
    }
}