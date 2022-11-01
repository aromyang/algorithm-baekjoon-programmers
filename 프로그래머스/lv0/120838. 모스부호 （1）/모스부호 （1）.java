import java.util.List;

class Solution {
    public String solution(String letter) {
        List<String> morse = List.of(".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..");
        String lang = "abcdefghijklmnopqrstuvwxyz";
        StringBuilder sb = new StringBuilder();

        String[] letters = letter.split(" ");

        for (String s : letters) {
            sb.append(lang.charAt(morse.indexOf(s)));
        }

        return sb.toString();
    }
}