import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> list = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        
        //약관 종류
        for (String term : terms) {
            String[] parts = term.split(" ");
            map.put(parts[0], Integer.parseInt(parts[1]));
        }
        
        //today 년월일 처리
        int year = Integer.parseInt(today.split("\\.")[0]);
        int month = Integer.parseInt(today.split("\\.")[1]);
        int day = Integer.parseInt(today.split("\\.")[2]);
        
        for (int i=0; i<privacies.length; i++){
            String[] parts = privacies[i].split(" ");
            String date = parts[0];
            int type = map.get(parts[1]) * 28;

            int num = (year - Integer.parseInt(date.split("\\.")[0]))*28*12
                +(month - Integer.parseInt(date.split("\\.")[1]))*28
                +(day - Integer.parseInt(date.split("\\.")[2]));
            
            if (num>=type){
                list.add(i+1);
            }
        }    return list.stream().filter(i->i!=null).mapToInt(i->i).toArray();

    }
}