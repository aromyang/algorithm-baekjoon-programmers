import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String s) {
        final Map<String, String> map = new HashMap<String, String>() {
            {
                put("0", "zero");
                put("1", "one");
                put("2", "two");
                put("3", "three");
                put("4", "four");
                put("5", "five");
                put("6", "six");
                put("7", "seven");
                put("8", "eight");
                put("9", "nine");
            }
        };

        for (Map.Entry<String, String> entry : map.entrySet()) {
            s = s.replaceAll(entry.getValue(), entry.getKey());
        }

        return Integer.parseInt(s);
    }
}