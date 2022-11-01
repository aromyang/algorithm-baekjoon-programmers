import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String my_string) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < my_string.length(); i++) {
            if (Character.isDigit(my_string.charAt(i))) {
                answer.add(my_string.charAt(i) - '0');
            }
        }

        return answer.stream().sorted().mapToInt(i -> i).toArray();
    }
}