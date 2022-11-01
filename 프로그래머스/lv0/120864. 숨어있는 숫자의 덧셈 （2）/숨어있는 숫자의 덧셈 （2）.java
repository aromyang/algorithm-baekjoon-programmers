import java.util.Arrays;

class Solution {
    public int solution(String my_string) {
        my_string = my_string.toLowerCase();
        my_string = my_string.replaceAll("[a-z]", " ");
        
        return Arrays.stream(my_string.split(" "))
                .filter(space -> !space.isBlank())
                .mapToInt(Integer::parseInt)
                .sum();
    }
}