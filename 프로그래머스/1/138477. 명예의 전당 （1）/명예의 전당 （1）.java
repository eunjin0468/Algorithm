import java.util.*;
class Solution {
    public List solution(int k, int[] score) {
        List<Integer> arr = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        for (int i=0; i<score.length; i++){
            if (arr.size() < k){
                arr.add(score[i]);
                Collections.sort(arr);
                ans.add(arr.get(0));
            }
            else{
                if (arr.get(0) < score[i]){
                    arr.set(0, score[i]);
                    Collections.sort(arr);
                    ans.add(arr.get(0));
                }
                else
                    ans.add(arr.get(0));
            }
        }
        return ans;
    }
}