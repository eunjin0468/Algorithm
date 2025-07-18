import java.util.*;
class Solution {
    public long solution(long n) {
        long answer = -1;
        
        for (long i=1; i<=n; i++){
            if (n==Math.pow(i,2)){
                answer = (long) Math.pow(i+1,2);
                break;
            }
        }
        return answer;
    }
}