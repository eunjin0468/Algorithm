class Solution {
    public String solution(String s) {
        StringBuilder res = new StringBuilder();
        
        int i = 0;
        
        for (int j=0; j<s.length(); j++){
            if (s.charAt(j) == ' ') {
                i = 0;
                res.append(' ');
            }
            else{
                if (i%2==0) {
                    res.append(String.valueOf(s.charAt(j)).toUpperCase());
                    i++;
                }
                else{
                    res.append(String.valueOf(s.charAt(j)).toLowerCase());
                    i++;
                }
            }
        }
        String answer = res.toString();
        return answer;
    }
}