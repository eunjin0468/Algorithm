import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        Map<String, Integer> need = new HashMap<>();
        Map<String, Integer> have = new HashMap<>();
        
        for(int i=0; i<want.length; i++){
            need.put(want[i], number[i]);
        }
        
        int total = 0;
        for(int x: number) total += x;
        if(total!=10 || discount.length<10) return 0;
        
        for (int i=0; i<10; i++){
            String item = discount[i];
            have.put(item, have.getOrDefault(item, 0)+1);
        }
        
        if(have.equals(need)) answer++;
        
        for(int i=10; i<discount.length; i++){
            String out = discount[i-10];
            String in = discount[i];
            
            Integer cntOut = have.get(out);
            if(cntOut != null){
                if(cntOut == 1) have.remove(out);
                else have.put(out, cntOut-1);
            }
            
            have.put(in,have.getOrDefault(in, 0)+1);
            
            if(have.equals(need)) answer++;
        }
        return answer;
    }
}