class Solution {
    public int[] solution(long n) {
        String[] str = Long.toString(n).split("");
        int[] answer = new int[str.length];
        for (int i=0; i<str.length; i++){
            answer[i] = Integer.parseInt(str[str.length-i-1]);
        }
        return answer;
    }
}