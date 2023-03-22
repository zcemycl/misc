class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        result = 0
        i,j = 0,0 
        visited = set()
        while i<=j and j<len(s):
            if s[j] not in visited:
                visited.add(s[j])
                result = max(result, j-i+1)
                j+=1
            else:
                visited.remove(s[i])
                i+=1
        return result

if __name__ == "__main__":
    inputs = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ]
    for s, expected in inputs:
        print(Solution.lengthOfLongestSubstring(s))