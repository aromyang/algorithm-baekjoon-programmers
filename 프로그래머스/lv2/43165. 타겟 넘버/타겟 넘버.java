class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }
    public static int dfs(final int[] numbers, final int target, int sum, int depth) {
        if (depth == numbers.length) {
            if (sum == target) {
                return 1;
            } else {
                return 0;
            }
        }

        return dfs(numbers, target, sum + numbers[depth], depth + 1)
                + dfs(numbers, target, sum - numbers[depth], depth + 1);
    }

}