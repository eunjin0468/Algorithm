import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for(int size: tangerine)
            countMap.put(size, countMap.getOrDefault(size, 0)+1);
        
        List<Integer> count = new ArrayList<>(countMap.values());
        count.sort(Collections.reverseOrder());
        
        int kinds = 0;
        int total = 0;
        for(int c: count){
            total+=c;
            kinds++;
            if(total>=k) break;
        }
        return kinds;
    }
}