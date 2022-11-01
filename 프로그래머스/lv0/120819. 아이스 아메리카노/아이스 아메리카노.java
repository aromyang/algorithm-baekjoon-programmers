class Solution {
    public int[] solution(int money) {
        int price = 5500;
        return new int[]{money / price, money % price};
    }
}