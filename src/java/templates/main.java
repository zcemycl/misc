class Solution {
    public int random = 5;
    private static int random2 = 10;
    int modelYear;

    public Solution(int year) {
        modelYear = year;
    }

    public void naive() {
        System.out.println("Hello World!");
        System.out.println(random2);
    }

    public static void naive2() {
        System.out.println("Hello World2!");
    }

    public static void naive3() {
        // System.out.println(random); // not accessible
        System.out.println(random2);
    }

    public static void main(String[] args) {
        Solution s = new Solution(2020);
        s.naive();
        naive2();
        naive3();
        System.out.println(s.random);
    }
}