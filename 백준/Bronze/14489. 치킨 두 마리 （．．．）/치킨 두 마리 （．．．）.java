import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int chicken = sc.nextInt();
        
        if (num1+num2 < chicken*2)
            System.out.print(num1+num2);
        else
            System.out.print((num1+num2)-(chicken*2));
    }
}