import java.util.*;

public class Main{
    static int arg[] = {4,2,3,3,3,3,3,3,3,3};
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while (true){
            String num = scanner.nextLine();
            int total = 1;
            if(num.equals("0"))
                break;
            for (int i=0; i<num.length(); i++){
                if(num.charAt(i)=='0')
                    total += 5;
                else if(num.charAt(i)=='1')
                    total += 3;
                else
                    total += 4;
            }
            System.out.println(total);
        }
    }
}