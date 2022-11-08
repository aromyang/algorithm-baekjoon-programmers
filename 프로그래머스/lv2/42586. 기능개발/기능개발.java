import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> pro = Arrays.stream(progresses).boxed().collect(Collectors.toList());
        List<Integer> answer = new ArrayList<>();

        int count = 0;
        int index = 0;

        while (!pro.isEmpty()) {
            for (int i = 0; i < progresses.length; i++) {
                progresses[i] += speeds[i];
            }

            if (progresses[index] >= 100) {
                for (; index < progresses.length; index++) {
                    if (progresses[index] < 100) {
                        break;
                    } else {
                        count++;
                        pro.remove(0);
                    }
                }
                answer.add(count);
            }
            count = 0;
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}