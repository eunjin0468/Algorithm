import java.util.Arrays;

class Solution {
    public long solution(long n) {
        String[] list = Long.toString(n).split("");
        Arrays.sort(list);
        StringBuilder sb = new StringBuilder();
        for (String str: list) sb.append(str);
        return Long.parseLong(sb.reverse().toString());
    }
}