import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public int solution(int a, int b) {
        if (a % b == 0) {
            return 1;
        }

        int gcd = gcd(a, b);
        b /= gcd;

        List<Integer> list = new ArrayList<>();

        for (int i = 2; i <= b; i++) {
            while (b % i == 0) {
                list.add(i);
                b /= i;
            }
        }

        list = list.stream().distinct().collect(Collectors.toList());

        return ((list.contains(2) || list.contains(5)) && list.size() <= 2) ? 1 : 2;    }
    
    public static int gcd(int n, int m) {
        if (n % m == 0) {
            return m;
        }
        return gcd(m, n % m);
    }

}