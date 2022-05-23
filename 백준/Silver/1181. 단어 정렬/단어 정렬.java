import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int testcase = Integer.parseInt(reader.readLine());
        String[] arr = new String[testcase];
        for(int i=0; i<testcase; i++){
            arr[i] = reader.readLine();
        }


        Arrays.sort(arr);
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.length() - s2.length();
            }
        });

        List<String> list = Arrays.asList(arr);

        list.stream()
                .distinct()
                .forEach(s -> System.out.println(s));
    }
}
