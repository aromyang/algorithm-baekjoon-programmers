import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> one = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> two = Arrays.asList(2, 1, 2, 3, 2, 4, 2, 5);
        List<Integer> three = Arrays.asList(3, 3, 1, 1, 2, 2, 4, 4, 5, 5);

        Map<Integer, Integer> map = new HashMap<>(Map.of(1, 0, 2, 0, 3, 0));

        int index1 = 0, index2 = 0, index3 = 0;

        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == one.get(index1++)) {
                map.put(1, map.get(1) + 1);
            }
            if (answers[i] == two.get(index2++)) {
                map.put(2, map.get(2) + 1);
            }
            if (answers[i] == three.get(index3++)) {
                map.put(3, map.get(3) + 1);
            }

            if (index1 >= one.size()) {
                index1 = 0;
            }
            if (index2 >= two.size()) {
                index2 = 0;
            }
            if (index3 >= three.size()) {
                index3 = 0;
            }
        }

        List<Map.Entry<Integer, Integer>> list = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .collect(Collectors.toList());

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < list.size() - 1; i++) {
            if (list.get(i).getValue() > list.get(i + 1).getValue()) {
                answer.add(list.get(i).getKey());
                break;
            } else if (Objects.equals(list.get(i).getValue(), list.get(i + 1).getValue())) {
                answer.add(list.get(i).getKey());
                if (i + 1 == list.size() - 1) {
                    answer.add(list.get(i + 1).getKey());
                }
            } else {
                break;
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}