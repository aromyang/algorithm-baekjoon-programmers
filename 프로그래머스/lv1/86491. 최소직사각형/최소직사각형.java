class Solution {
    public int solution(int[][] sizes) {
        int w = 0;
        int h = 0;

        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] < sizes[i][1]) {
                int temp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = temp;
            }
            w = Math.max(w, sizes[i][0]);
            h = Math.max(h, sizes[i][1]);
        }

        return w * h;
    }
}