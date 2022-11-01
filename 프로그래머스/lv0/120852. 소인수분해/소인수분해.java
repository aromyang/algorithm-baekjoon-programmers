import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<>();
        int i = 2;
        while (n != 1) {
            if (n % i != 0) {
                i++;
            } else {
                n /= i;
                answer.add(i);
            }
        }
        return answer.stream().distinct().mapToInt(j -> j).toArray();
    }
}