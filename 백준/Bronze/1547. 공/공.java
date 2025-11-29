import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int result = 1;
        for(int i=0; i<t; i++){
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();
            
            if(num1==result){
                result=num2;
            }
            else if(num2==result){
                result=num1;
            }
        }
        System.out.print(result);
    }
}