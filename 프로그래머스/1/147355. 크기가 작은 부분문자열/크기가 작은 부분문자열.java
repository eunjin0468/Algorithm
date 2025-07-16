class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        for (int i=0; i<t.length()-p.length()+1; i++){
            String tmp = t.substring(i, i+p.length());
            if (tmp.length() <= p.length() && tmp.compareTo(p) <= 0)
                answer++;
        }
        return answer;
    }
}