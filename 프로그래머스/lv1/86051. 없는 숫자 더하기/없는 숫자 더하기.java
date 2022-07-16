import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        List<Integer> list = Arrays.stream(numbers).boxed().collect(Collectors.toList());

        int sum = 0;

        for (int i = 1; i <= 9; i++) {
            if(!list.contains(i)) sum += i;
        }
        
        return sum;
    }
}