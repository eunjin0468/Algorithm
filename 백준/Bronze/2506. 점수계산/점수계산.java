import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        int num = scanner.nextInt();
        int tmp = 0;
        int sum = 0;
        
        for(int i=0; i<num; i++){
            int x = scanner.nextInt();
            
            if(x==1){
                tmp+=1;
                sum+=tmp;
            }
            else{
                tmp=0;
            }
        }
        System.out.println(sum);
    }
}