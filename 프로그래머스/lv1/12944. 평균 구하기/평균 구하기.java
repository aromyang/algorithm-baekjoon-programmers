import java.util.Arrays;

class Solution {
    public double solution(int[] arr) {
        double avg = Arrays.stream(arr)
                .average()
                .getAsDouble();

        return avg == (int) avg ? (int) avg : avg;
    }
}