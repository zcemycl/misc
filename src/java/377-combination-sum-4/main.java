import java.util.Arrays;

class Solution {
    public static int dp(int[] nums, int target){
        int[] dps = new int[target+1];
        Arrays.fill(dps, 0);
        dps[0] = 1;
        for (int i=1; i<target+1; i++) {
            for (int num : nums) {
                if (i-num >= 0)
                    dps[i] += dps[i-num];
            }
        }
        System.out.println(Arrays.toString(dps));
        return dps[target];
    }

    public static void main(String[] args) {
        
        System.out.println(
            dp(new int[] {1,2,3}, 4)
        );
    }
}

// class Solution:
//     @staticmethod
//     def dp(nums, target):
//         dps = [0 for _ in range(target+1)]
//         dps[0] = 1
//         for i in range(1, target+1):
//             for num in nums:
//                 if i-num>=0:
//                     dps[i] += dps[i-num]
//         return dps[-1]

// if __name__ == "__main__":
//     inputs = [
//         ([1,2,3],4,7),
//         ([9],3,0)
//     ]
//     for nums, target, expected in inputs:
//         print(Solution.dp(nums, target))