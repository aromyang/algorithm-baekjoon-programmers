import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        Map<String, List<Map<Integer, Integer>>> map = new HashMap<>();
        Map<String, Integer> counting = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            map.put(genres[i], map.getOrDefault(genres[i], new ArrayList<>()));
            map.get(genres[i]).add(Map.of(i, plays[i]));

            counting.put(genres[i], counting.getOrDefault(genres[i], 0) + plays[i]);
        }

        List<Map.Entry<String, Integer>> collect = counting.entrySet().stream()
                .sorted(Collections.reverseOrder(Map.Entry.comparingByValue()))
                .collect(Collectors.toList());

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < collect.size(); i++) {
            List<Map<Integer, Integer>> list = map.get(collect.get(i).getKey());
            if (list.size() == 1) {
                answer.add(list.get(0).keySet().iterator().next());
                continue;
            }

            list.sort((o1, o2) -> {
                Integer key1 = o1.keySet().iterator().next();
                Integer key2 = o2.keySet().iterator().next();
                return o2.get(key2) - o1.get(key1);
            });

            answer.add(list.get(0).keySet().iterator().next());
            answer.add(list.get(1).keySet().iterator().next());
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}