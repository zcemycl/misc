import java.util.Hashtable;
import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    private Hashtable<Integer, List<Integer>> adjls;
    private Hashtable<Integer, Boolean> cache;
    private void convert_to_adjacent_list(int[][] prerequisites) {
        this.adjls = new Hashtable<>();
        for (int[] prerequisite: prerequisites) {
            List<Integer> requires = adjls.getOrDefault(prerequisite[0], new ArrayList<Integer>());
            requires.add(prerequisite[1]);
            this.adjls.put(prerequisite[0], requires);
        }
    }
    private boolean dfs(int i, HashSet<Integer> visited) {
        if (this.adjls.getOrDefault(i, new ArrayList<Integer>()).size() == 0) {
            this.cache.put(i, true);
            return true;
        }
        if (visited.contains(i)) 
            return false;
        HashSet newVisited = new HashSet();
        newVisited = (HashSet)visited.clone();
        newVisited.add(i);
        if (this.cache.containsKey(i))
            return this.cache.get(i);
        for (int child : this.adjls.getOrDefault(i, new ArrayList<Integer>())) {
            boolean isFinish = this.dfs(child, newVisited);
            this.cache.put(child, isFinish);
            if (! isFinish)
                return false;
        }
        return true;
    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        this.convert_to_adjacent_list(prerequisites);
        this.cache = new Hashtable<>();
        for (int i=0; i<numCourses; i++){
            boolean isFinish = this.dfs(i, new HashSet<Integer>());
            this.cache.put(i, isFinish);
            if (! isFinish)
                return false;
        }
        return true;
    }
}