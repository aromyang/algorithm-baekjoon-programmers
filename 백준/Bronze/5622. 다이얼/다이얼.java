import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] str = new String[] {"ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};

        int[] strToInt = new int[str.length];
        for(int i=0; i<str.length; i++){
            strToInt[i] = i+3;
        }


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String dial = br.readLine();

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
