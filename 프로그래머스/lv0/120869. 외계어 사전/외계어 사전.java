import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(String[] spell, String[] dic) {
        List<String> list = Arrays.stream(dic)
                .filter(a -> a.length() == spell.length)
                .collect(Collectors.toList());

        Arrays.sort(spell);
        String sp = Arrays.toString(spell);

        int answer = 0;

        for (String s : list) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            if (Arrays.toString(chars).equals(sp)) {
                answer = 1;
                break;
            }
        }

        return answer == 1 ? 1 : 2;
    }
}