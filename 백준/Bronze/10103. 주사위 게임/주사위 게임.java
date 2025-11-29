import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int res1 = 100;
        int res2 = 100;
        
        for(int i=0; i<t; i++){
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();
            
            if(num1<num2){
                res1-=num2;
            }
            else if(num1>num2){
                res2-=num1;
            }
        }
        System.out.print(res1+"\n"+res2);
    }
}