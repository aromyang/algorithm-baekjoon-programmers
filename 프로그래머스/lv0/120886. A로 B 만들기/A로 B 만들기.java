class Solution {
    public int solution(String before, String after) {
        int count = 0;
        for (int i = 0; i < after.length(); i++) {
            for (int j = 0; j < before.length(); j++) {
                if (after.charAt(i) == before.charAt(j)) {
                    count++;
                    before = before.replaceFirst(Character.toString(before.charAt(j)), "");
                    break;
                }
            }
        }
        return count == after.length() ? 1 : 0;
    }
}