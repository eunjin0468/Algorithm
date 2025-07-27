class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] ch = s.toCharArray();
        for (char c:ch){
            if (c==32){
                answer+=" ";
            }else{
                if (c<=90){ //대문자일때
                    c+=n;
                    if (c>90) // z넘어갈때
                            c-=26;
                }else{
                    c+=n;
                    if (c>122)
                        c-=26;
                }answer+=c;
            }
        }
        return answer;
    }
}