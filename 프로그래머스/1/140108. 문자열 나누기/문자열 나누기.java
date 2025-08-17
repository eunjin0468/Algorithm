class Solution {
    public int solution(String s) {
        int answer = 0;
        char one = ' ';
        int same = 0;
        int diff = 0;
        
        for (int i=0; i<s.length(); i++){
            if (one == ' '){
                one = s.charAt(i);
            }
            if (one == s.charAt(i)){
                same++;
            }else{
                diff++;
            }
            if (same==diff){
                answer++;
                one = ' ';
                same = 0;
                diff = 0;
            }
        }
        if (same!=0){
            answer++;
        }
        if (answer==0){
            answer=1;
        }
        return answer;
    }
}