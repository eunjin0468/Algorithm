class Solution {
    public String solution(int a, int b) {
        String[] day = {"FRI","SAT", "SUN","MON","TUE","WED","THU"};
        int[] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 30};
        int ans = 0;
        
        for (int i=0; i<a-1; i++){
            ans+=month[i];
        }
        ans+=b-1;
        
        return day[ans%7];
    }
}