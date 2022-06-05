import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static boolean[][] chess;
    public static int min = 64;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int rows = Integer.parseInt(st.nextToken());
        int cols = Integer.parseInt(st.nextToken());

        chess = new boolean[rows][cols];

        for(int i=0; i<rows; i++){
            String colors = br.readLine();
            for(int j=0; j<cols; j++){
                if(colors.charAt(j)=='W') chess[i][j] = true;
                else chess[i][j] = false;
            }
        }

        int rowMin = rows-8;
        int colMin = cols-8;

        for(int i=0; i<=rowMin; i++){
            for(int j=0; j<=colMin; j++){
                verifying(i, j);
            }
        }
        System.out.println(min);
    }

    public static void verifying(int row, int col){
        int rowMax = row+7;
        int colMax = col+7;
        int count = 0;

        boolean verify = chess[rowMax][colMax];
        
        for(int i=row; i<=rowMax; i++){
            for(int j=col; j<=colMax; j++){
                if(chess[i][j]!=verify){
                    count++;
                }
                verify = !verify;
            }
            verify = !verify;
        }
        count = Math.min(count, 64-count);
        min = Math.min(min, count);
    }
    
}
