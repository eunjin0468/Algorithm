import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> arr = new ArrayList<Integer>();
        int max = 0;
        int min = 1000;
        for(int i=1; i<=n; i++){
            arr.add(sc.nextInt());
        }
        System.out.println(Collections.max(arr)-Collections.min(arr));        
    }
}