import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < operations.length; i++) {
            if (operations[i].startsWith("I")) {
                list.add(Integer.parseInt(operations[i].substring(2)));
                list.sort(Comparator.naturalOrder());
            } else if (operations[i].startsWith("D") && !list.isEmpty()) {
                if (operations[i].substring(2).equals("1")) {
                    list.remove(list.size() - 1);
                } else {
                    list.remove(0);
                }
            }
        }

        if (list.isEmpty()) {
            return new int[]{0, 0};
        } else if (list.size() == 1) {
            return new int[]{list.get(0), list.get(0)};
        } else {
            return new int[]{list.get(list.size() - 1), list.get(0)};
        }
    }
}