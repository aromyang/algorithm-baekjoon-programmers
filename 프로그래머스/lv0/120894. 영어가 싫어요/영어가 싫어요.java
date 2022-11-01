import java.util.Map;

class Solution {
    public long solution(String numbers) {
        StringBuilder sb = new StringBuilder();
        Map<String, Integer> map = Map.of(
                "zero", 0,
                "one", 1,
                "two", 2,
                "three", 3,
                "four", 4,
                "five", 5,
                "six", 6,
                "seven", 7,
                "eight", 8,
                "nine", 9
        );

        int start = 0;
        int end = 2;

        for (int i = 0; i < numbers.length(); i++) {
            String sub = numbers.substring(start, end - 1);
            if (map.containsKey(sub)) {
                sb.append(map.get(sub));
                start = i + 1;
                end = start + 2;
            } else {
                end++;
            }
        }
        return Long.parseLong(String.valueOf(sb));
    }
}