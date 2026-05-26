class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, win = {}, {}
        right, left = 0, 0
        valid = 0
        min_length = float("inf")

        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        print(target)

        while right < len(s):
            c = s[right]
            right += 1
            if c in target:
                win[c] = win.get(c, 0) + 1
                if win[c] == target[c]:
                    valid += 1
                print(valid)
            while valid == len(target):
                if right - left <  min_length:
                    start = left
                    min_length = right - left
                d = s[left]
                left += 1
                if d in target:
                    if win[d] == target[d]:
                        valid -= 1
                    win[d] = win.get(d, 0) - 1
                    
        # print(left, right)    
        if min_length == float("inf"):
            return ""
        else:
            return s[start : start+min_length]