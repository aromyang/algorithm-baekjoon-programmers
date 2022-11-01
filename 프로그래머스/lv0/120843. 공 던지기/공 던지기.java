class Solution {
    public int solution(int[] numbers, int k) {
        int num = k * 2 - 1;
        int order = k * 2 - 1 >= numbers.length ? num % numbers.length : num;
        
        return numbers[order - 1];
    }
}