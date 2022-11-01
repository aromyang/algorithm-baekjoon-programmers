import java.math.BigInteger;

class Solution {
    public String solution(String bin1, String bin2) {
        BigInteger b1 = new BigInteger(bin1, 2);
        BigInteger b2 = new BigInteger(bin2, 2);

        return add(b1, b2).toString(2);
    }
    
    public static BigInteger add(BigInteger b1, BigInteger b2) {
        if (b2 == BigInteger.ZERO) {
            return b1;
        }
        BigInteger sum = b1.xor(b2);
        BigInteger shift = b1.and(b2).shiftLeft(1);
        return add(sum, shift);
    }

}