import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int a : array) {
            map.put(a, map.getOrDefault(a, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> list = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .collect(Collectors.toList());

        if (list.size() == 1) {
            return list.get(0).getKey();
        } else if (list.get(0).getValue() == list.get(1).getValue()) {
            return -1;
        } else {
            return list.get(0).getKey();
        }
    }
}