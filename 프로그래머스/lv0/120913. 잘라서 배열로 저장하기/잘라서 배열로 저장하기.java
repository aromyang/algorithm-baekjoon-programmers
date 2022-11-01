class Solution {
    public String[] solution(String my_str, int n) {
        int size = my_str.length() % n == 0 ? my_str.length() / n : my_str.length() / n + 1;

        String[] answer = new String[size];

        int start = 0;

        for (int i = 0; i < size; i++) {
            if (start + n >= my_str.length()) {
                answer[i] = my_str.substring(start);
            } else {
                answer[i] = my_str.substring(start, start + n);
            } 
            start += n;
        }

        return answer;
    }
}