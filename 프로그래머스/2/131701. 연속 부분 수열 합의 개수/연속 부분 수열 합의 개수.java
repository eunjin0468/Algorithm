import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int n = elements.length;

        int[] ext = new int[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            ext[i] = elements[i % n];
        }

        int[] ps = new int[2 * n + 1];
        for (int i = 1; i <= 2 * n; i++) {
            ps[i] = ps[i - 1] + ext[i - 1];
        }

        // 3) 모든 길이에 대해 가능한 합을 Set에 저장
        Set<Integer> sums = new HashSet<>();

        for (int len = 1; len <= n; len++) {         
            for (int start = 0; start < n; start++) { 
                int sum = ps[start + len] - ps[start];
                sums.add(sum);
            }
        }

        return sums.size();
    }
}
