class Solution {
    public int solution(int[] common) {
        String type = common[2] - common[1] == common[1] - common[0] ? "a" : "b";

        switch (type) {
            case "a" :
                return common[common.length - 1] + (common[1] - common[0]);
            case "b" :
                return common[common.length - 1] * (common[1] / common[0]);
        }
        
        return 0;
    }
}