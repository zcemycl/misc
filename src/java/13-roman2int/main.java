import java.util.Hashtable;

class Solution {
    public int romanToInt(String s) {
        Hashtable<Character, Integer> map_roman_int = new Hashtable<>();
        map_roman_int.put('I', 1);
        map_roman_int.put('V', 5);
        map_roman_int.put('X', 10);
        map_roman_int.put('L', 50);
        map_roman_int.put('C', 100);
        map_roman_int.put('D', 500);
        map_roman_int.put('M', 1000);
        int num_characters = s.length();
        int result = map_roman_int.get(s.charAt(num_characters-1));
        for (int i=num_characters-2; i>=0; i--){
            if (map_roman_int.get(s.charAt(i))<map_roman_int.get(s.charAt(i+1)))
                result -= map_roman_int.get(s.charAt(i));
            else
                result += map_roman_int.get(s.charAt(i));
        }
        return result;
    }
}