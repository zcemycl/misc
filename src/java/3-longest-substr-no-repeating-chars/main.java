import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0,j = 0,result = 0;
        HashSet<Character> visited = new HashSet<>();
        while (i<=j && j<s.length()){
            if (! visited.contains(s.charAt(j))) {
                visited.add(s.charAt(j));
                result = Math.max(result, j-i+1);
                j+=1;
            } else {
                visited.remove(s.charAt(i));
                i+=1;
            }
        }
        return result;
    }
}