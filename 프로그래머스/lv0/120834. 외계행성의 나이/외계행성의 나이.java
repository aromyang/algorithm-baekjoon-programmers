class Solution {
    public String solution(int age) {
        String nums = "abcdefghij";
        String ages = String.valueOf(age);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < ages.length(); i++) {
            sb.append(nums.charAt((char)(ages.charAt(i) - '0')));
        }

        return String.valueOf(sb);
    }
}