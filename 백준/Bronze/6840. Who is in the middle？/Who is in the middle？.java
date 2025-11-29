import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();
        Integer[] arr = {num1, num2, num3};
        Arrays.sort(arr);
        System.out.print(arr[1]);
    }
}