class Solution {
    public String solution(String my_string, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            char single = my_string.charAt(i);
            sb.append(Character.toString(single).repeat(n));
        }
        return String.valueOf(sb);
    }
}