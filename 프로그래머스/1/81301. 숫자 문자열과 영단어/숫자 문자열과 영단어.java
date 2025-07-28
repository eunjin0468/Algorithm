import java.util.*;

class Solution {
    public int solution(String s) {
        
        String[] en = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        
        for (int i=0; i<en.length; i++){
            if (s.contains(en[i])){
                s=s.replace(en[i], Integer.toString(i));
            }
        }
        return Integer.parseInt(s);
    }
}