class Solution {
    public String solution(String s) {
        String ans = "";
        String[] arr = s.split(" ");
        
        for (int i=0; i<arr.length; i++){
            String now = arr[i];
            
            if (now.length()==0)
                ans += " ";
            else{
                ans += now.substring(0,1).toUpperCase();
                ans += now.substring(1, now.length()).toLowerCase();
                ans += " ";
        }
    }
        if(s.substring(s.length()-1, s.length()).equals(" ")){
            return ans;
        }
        return ans.substring(0, ans.length()-1);
    }
}