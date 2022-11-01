import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        List<Character> list = s.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toList());
        char[] chars = s.toCharArray();
        Arrays.sort(chars);
        s = Arrays.toString(chars);

        for (int i = 0; i < s.length(); i++) {
            int finalI = i;
            String finalS = s;
            long count = list.stream()
                    .filter(a -> a == finalS.charAt(finalI))
                    .count();
            if (count == 1) {
                sb.append(s.charAt(i));
            }
        }

        return String.valueOf(sb);
    }
}