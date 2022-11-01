import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];

        Map<Integer, Double> map = new HashMap<>();
        for (int i = 0; i < score.length; i++) {
            double avg = ((double) score[i][0] + score[i][1]) / 2;
            map.put(i + 1, avg);
        }
        List<Map.Entry<Integer, Double>> list = map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .collect(Collectors.toList());

        System.out.println("list = " + list);

        answer[list.get(0).getKey() - 1] = 1;

        for (int i = 1; i < list.size(); i++) {
            if (Objects.equals(list.get(i).getValue(), list.get(i - 1).getValue())) {
                answer[list.get(i).getKey() - 1] = answer[list.get(i-1).getKey() - 1];
            } else {
                answer[list.get(i).getKey() - 1] = i + 1;
            }
        }

        return answer;
    }
}