class Solution {
    public int solution(String A, String B) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < A.length(); i++) {
            String sub = A.substring(0, A.length() - i);
            answer++;
            if (B.contains(sub)) {
                sb.append(sub);
                sb.insert(0, A.substring(A.length() - i));
                break;
            }
        }
        return String.valueOf(sb).equals(B) ? answer - 1 : - 1;
    }
}