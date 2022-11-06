class Solution {
    public String solution(String[] id_pw, String[][] db) {
        for (String[] s : db) {
            if (s[0].equals(id_pw[0]) && s[1].equals(id_pw[1])) {
                return "login";
            } else if (s[0].equals(id_pw[0])) {
                return "wrong pw";
            }
        }
        return "fail";
    }
}