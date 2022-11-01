class Solution {
    public String solution(String my_string) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < my_string.length(); i++) {
            char now = my_string.charAt(i);
            if (now >= 65 && now <= 90) {
                sb.append((char)(now + 32));
            } else {
                sb.append((char)(now - 32));
            }
        }
        return String.valueOf(sb);
    }
}