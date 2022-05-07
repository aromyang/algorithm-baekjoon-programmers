import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int time = sc.nextInt();

        if(time>=60){
            hour += (time/60);
            minute += (time%60);
            if(minute>=60){
                minute = minute-60;
                hour++;
            }
        } else{
            minute += time;
            if(minute>=60){
                minute -=60;
                hour++;
            }
        }
        if(hour>=24){
            if(hour%24==0){
                hour=0;
            } else{
                hour=hour%24;
            }
        }
        System.out.println(hour + " " + minute);
    }
}
