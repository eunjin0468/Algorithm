class Solution {
    public String solution(String s) {
        String[] arr = s.split(" ");
        
        int max = Integer.parseInt(arr[0]);
        int min = Integer.parseInt(arr[0]);
        
        for(String str:arr){
            int tmp = Integer.parseInt(str);
            if(tmp>max){
                max = tmp;
            }
            if(tmp<min){
                min = tmp;
            }
        }
        return min+" "+max;
    }
}