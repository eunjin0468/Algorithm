import java.util.*;

class Solution{
    public int solution(int[][] maps){        
        int[] dr = {1,-1,0,0};
        int[] dc = {0,0,-1,1};
        
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        
        Queue<int[]> q = new LinkedList<>();
        
        q.add(new int[]{0,0});
        visited[0][0] = true;                    
        
        while (!q.isEmpty()){
            int[] cur = q.poll();
            int r = cur[0];
            int c = cur[1];
            
            if(r==maps.length-1 && c==maps[0].length-1) return maps[r][c];
            
            for(int i=0; i<4; i++){
                int nr = r+dr[i];
                int nc = c+dc[i];
                
                if (nr<0 || nc<0 || nr>=maps.length || nc>=maps[0].length) continue;
                if (maps[nr][nc]==0) continue;
                if (visited[nr][nc]==true) continue;
                                
                visited[nr][nc] = true;
                maps[nr][nc] = maps[r][c]+1;
                q.add(new int[]{nr,nc});
            }
        }
        return -1;
    }
}