class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        win = {}
        left, right = 0, 0
        max_freq = 0
        max_result = 0

        while right < len(s):
            c = s[right]
            right += 1
            win[c] = win.get(c, 0) + 1
            max_freq = max(win[c], max_freq)
            while right - left - max_freq > k:
                d = s[left]
                left += 1
                win[d] = win.get(d, 0) - 1
            max_result = max(right - left, max_result)

        return max_result