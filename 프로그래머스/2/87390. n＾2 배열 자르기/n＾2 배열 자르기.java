import java.util.*;
class Solution {
    public int[] solution(int n, long left, long right) {
        int len = (int)(right-left+1);
        int[] ans = new int[len];
        
        for(long idx=left, p=0; idx<=right; idx++, p++){
            long r = idx/n;
            long c = idx%n;
            ans[(int)p] = (int)(Math.max(r,c)+1);
        }
        return ans;     
    }
}