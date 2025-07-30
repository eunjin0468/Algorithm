import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] ans = new int[commands.length];
        int size = commands.length;
        
        for (int i=0; i<size; i++){
            int start = commands[i][0]-1;
            int end = commands[i][1];
            int k = commands[i][2]-1; 
            
            int[] tmp = Arrays.copyOfRange(array, start, end);
            Arrays.sort(tmp);
            ans[i] = tmp[k];
        }
        return ans;
    }
}