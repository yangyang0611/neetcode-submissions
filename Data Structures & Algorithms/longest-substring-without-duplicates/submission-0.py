class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        win = {}
        max_count, count = 0, 0

        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1
            print(win)
            while win[c] > 1:
                d = s[left]
                left += 1
                win[d] = win.get(d, 0) - 1
            count = right - left
            max_count = max(count, max_count)
                
        return max_count