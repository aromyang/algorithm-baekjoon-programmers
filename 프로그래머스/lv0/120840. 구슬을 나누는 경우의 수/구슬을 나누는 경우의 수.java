import java.math.BigInteger;

class Solution {
    public int solution(int balls, int share) {
        BigInteger a = fac(balls);
        BigInteger b = fac(balls - share);
        BigInteger c = fac(share);

        String s = String.valueOf(a.divide(b.multiply(c)));
        return Integer.parseInt(s);
    }
    
    public static BigInteger fac(int n) {
        if (n <= 1) {
            return BigInteger.ONE;
        } else {
            return fac(n-1).multiply(BigInteger.valueOf(n));
        }
    }

}