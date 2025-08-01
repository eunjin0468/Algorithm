import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int [numbers.length+1];
        List <Integer> arr = new ArrayList<>();
        for (int i=0; i<numbers.length; i++){
            for (int j=i+1; j<numbers.length; j++){
                if (!arr.contains(numbers[i]+numbers[j]))
                    arr.add(numbers[i]+numbers[j]);
            }
        }
        return arr.stream().sorted().mapToInt(i->i).toArray();
    }
}