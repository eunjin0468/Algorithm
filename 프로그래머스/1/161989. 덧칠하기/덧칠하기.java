class Solution {
    public int solution(int n, int m, int[] section) {
        int ans = 0;
        int start = section[0];
        ans++;
        
        for (int item:section){
            if (start+m > item) continue;
            ans++;
            start = item;
        }
        return ans;
    }
}