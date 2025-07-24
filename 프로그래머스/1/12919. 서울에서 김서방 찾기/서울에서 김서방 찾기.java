class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
        int index = 0;
        for (index = 0; index<seoul.length; index++){
            if (seoul[index].equals("Kim"))
                break;
        }
        answer = "김서방은 "+index+"에 있다";
        return answer;
    }
}