class Solution {
    public boolean solution(int x) {
        int sum=0;
        String str = Integer.toString(x);
        for (int i=0; i<str.length(); i++){
            sum+=Character.getNumericValue(str.charAt(i));
        }
        System.out.print(sum);
        if (x%sum==0)
            return true;
        else   
            return false;
    }
}