class Solution { 
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder();
        for (int i=1; i<food.length; i++){ //0번 인덱스는 항상 1이므로 제외
            int cnt = food[i]/2;
            sb.append(String.valueOf(i).repeat(cnt));
        }
        String answer = sb+"0";
        return answer+=sb.reverse();
    }
}