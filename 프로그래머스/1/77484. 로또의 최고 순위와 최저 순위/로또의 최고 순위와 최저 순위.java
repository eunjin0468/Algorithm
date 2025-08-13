import java.util.*;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int tmp=0;
        int zero=0;
        
        for (int i = 0; i < 6; i++) {
            for (int j=0; j<6; j++){
                if(lottos[i]==win_nums[j]){
                    tmp++;
                }
            }
            if(lottos[i]==0)
                    zero++;
        }
        return new int[]{
            getRank(tmp+zero),
            getRank(tmp)
        };
    }

    private int getRank(int tmp){
        return switch(tmp){
            case 6 -> 1;
            case 5 -> 2;
            case 4 -> 3;
            case 3 -> 4;
            case 2 -> 5;
            case 1 -> 6;
            default -> 6;
        };
    }
}