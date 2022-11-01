import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] numlist, int n) {
        List<Integer> list = Arrays.stream(numlist).boxed()
                .collect(Collectors.toList());
        list.add(n);
        Collections.sort(list);

        List<Integer> answer = new ArrayList<>();

        int std = list.indexOf(n);
        int before = 1;
        int after = 1;

        for (int i = 0; i < list.size(); i++) {
            if (std - before < 0) {
                answer.addAll(list.subList(std + after, list.size()));
                break;
            } else if (std + after >= list.size()) {
                answer.add(list.get(std - before));
                before++;
                continue;
            }

            int i1 = list.get(std - before) - n;
            int i2 = list.get(std + after) - n;

            if (Math.abs(i2) <= Math.abs(i1)) {
                answer.add(i2 + n);
                after++;
            } else {
                answer.add(i1 + n);
                before++;
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}