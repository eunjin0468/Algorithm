import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for(int i=0; i<t; i++){
            int n = scanner.nextInt();
            HashMap<Integer, Boolean> rooms = new HashMap<>();
            
            for(int j=1; j<=n; j++){
                rooms.put(j, false);
            }
            
            for(int round=1; round<=n; round++){
                for(int room=round; room<=n; room+=round){
                    boolean isOpen = rooms.get(room);
                    rooms.put(room, !isOpen);
                }
            }
            int escapedStudents = 0;
            for (boolean isOpen:rooms.values()){
                if(isOpen){
                    escapedStudents++;
                }
            }
            System.out.println(escapedStudents);
        }
    }
}