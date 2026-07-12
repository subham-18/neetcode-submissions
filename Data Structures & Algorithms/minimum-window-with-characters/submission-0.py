class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        have, need_count = 0, len(need)  # distinct chars we need to satisfy
        result, result_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # if this char is one we need, and we just hit the exact required count
            if ch in need and window[ch] == need[ch]:
                have += 1

            # try shrinking while window is fully valid
            while have == need_count:
                # update result if this window is smaller
                if (right - left + 1) < result_len:
                    result = [left, right]
                    result_len = right - left + 1

                # shrink from left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                left += 1

        l, r = result
        return s[l : r + 1] if result_len != float("inf") else ""
