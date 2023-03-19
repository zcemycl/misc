class Solution:
    @classmethod 
    def naive(cls, nums):
        cls.result = 0
        L = len(nums)
        def dfs(i, count, prev, members):
            if i==L:
                print(members, count)
                cls.result = max(cls.result, count)
                return
            if nums[i]>prev:
                dfs(i+1, count+1, nums[i], members+[nums[i]])
            dfs(i+1, count, prev, members)
        dfs(0, 0, -10**5, [])
        return cls.result
    
    @classmethod
    def dp(cls, nums):
        L = len(nums)
        dps = [1 for i in range(L)]
        for i in range(L-1, -1, -1):
            for j in range(i+1, L):
                if nums[i]>=nums[j]:
                    continue
                dps[i] = max(1+dps[j], dps[i])
        print(dps)
        return max(dps)


if __name__ == "__main__":
    inputs = [
        ([10,9,2,5,3,7,101,18], 4),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1)
    ]
    for nums, expected in inputs:
        # print("Final: ", Solution.naive(nums))
        print(Solution.dp(nums))