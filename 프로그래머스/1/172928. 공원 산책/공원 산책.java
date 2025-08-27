class Solution {
    public int[] solution(String[] park, String[] routes) {
        int h = park.length; //세로
        int w = park[0].length(); //가로
        
        int sh = 0;
        int sw = 0;
        
        //시작 지점 찾기
        for(int i=0; i<park.length; i++){
            if (park[i].contains("S")){
                sh = i;
                sw = park[i].indexOf('S');
            }
        }
        
        for (String route : routes){
            int nh = sh;
            int nw = sw;
            int dir = route.charAt(0);
            int move = Character.getNumericValue(route.charAt(2));
            
            for(int i=0; i<=move; i++){
                if(dir=='N') nh--;
                if(dir=='S') nh++;
                if(dir=='W') nw--;
                if(dir=='E') nw++;
                
                if (nh>=0 && nh<h && nw>=0 && nw<w){
                    if(park[nh].charAt(nw)=='X') break;
                    
                    if(i==move-1){
                        sh=nh;
                        sw=nw;
                    }
                }
            }
        }
    
            int[] answer = new int[2];
            answer[0] = sh;
            answer[1] = sw;
            return answer;
    }
}