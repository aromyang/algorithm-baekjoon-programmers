import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String[] str = new String[] {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
        
        int[] strToInt = new int[str.length];
        for(int i=0; i<str.length; i++){
            strToInt[i] = i+3;
        }

        Scanner sc = new Scanner(System.in);

        String dial = sc.next();

        char[] dialArr = new char[dial.length()];

        for(int i=0; i<dialArr.length; i++) {
            dialArr[i] = dial.charAt(i);
        }
        
        int time = 0;

        for(int i=0; i<str.length; i++){
            for(int j=0; j<str[i].length(); j++){
                for(int k=0; k<dialArr.length; k++){
                    if(str[i].charAt(j)==dialArr[k]){
                        time += strToInt[i];
                    }
                }
            }
        }



        System.out.println(time);

    }
}
