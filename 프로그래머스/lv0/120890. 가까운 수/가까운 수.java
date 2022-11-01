import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] array, int n) {
        List<Integer> list = Arrays.stream(array)
                .boxed()
                .collect(Collectors.toList());
        list.add(n);
        list.sort(Comparator.comparingInt(o -> o));
        int std = list.indexOf(n);

        if (std == 0) return list.get(1);
        if (std == list.size() - 1) return list.get(list.size() - 2);

        Integer before = list.get(std - 1);
        Integer after = list.get(std + 1);

        return n - before <= after - n ? before : after;
    }
}